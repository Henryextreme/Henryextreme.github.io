##########################################################
####        N A V I O    C A T A    M O E D A S       ####
##########################################################
#### Prof. Filipo Novo Mor - filipomor.com            ####
#### github.com/ProfessorFilipo                       ####
##########################################################
import pygame
import random
import sys
from pathlib import Path

pygame.init()

#  carrega os sons
som_aviso = pygame.mixer.Sound(r'CatchTheCoin\Assets/Audio/notificacao.mp3')
som_beep = pygame.mixer.Sound(r'CatchTheCoin\Assets/Audio/beep.mp3')

#
# Configurações iniciais
#
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)
CAMINHAO_TAMANHO = (100, 100)

# Carregar a imagem do fundo (altere o caminho para sua imagem real)
background_img = pygame.image.load(r'CatchTheCoin\Assets2\Road\Road_00.png')
background_img = pygame.transform.scale(background_img, (HEIGHT, background_img.get_height()))
background_img = pygame.transform.scale(background_img, (WIDTH, background_img.get_width()))
background_img = pygame.transform.rotate(background_img, 90)


# barco
barco_sprite_img = pygame.image.load(r'CatchTheCoin/Assets2/Fusca.png').convert_alpha()
# Opcionalmente, ajuste o tamanho do sprite
barco_sprite_img = pygame.transform.smoothscale(barco_sprite_img, (54*1.25, 85*1.25))


#
# Função para configurar a dificuldade
#
qtd_caminhao = 2
if clock > 20:
    qtd_caminhao = 10


# Classe das Caminhao animadas
class Caminhao(pygame.sprite.Sprite):
    def __init__(self, x, y, tipo, v_min, v_max):
            super().__init__()
            # 1) Carrega a imagem do caminhão
            self.image = pygame.image.load('CatchTheCoin\Assets2\Caminhao.png').convert_alpha()
            # 2) Ajusta o tamanho
            self.image = pygame.transform.scale(self.image, (57*2, 86*2))
            # 3) Cria o rect a partir da imagem, posicionando em (x,y)
            self.rect = self.image.get_rect(topleft=(x, y))
            # 4) Defina uma velocidade aleatória
            self.speed = random.randint(v_min, v_max)
    def update(self):
        self.rect.y += self.speed
        # quando sair da tela embaixo, você pode resetar para o topo:
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-100, -10)
            self.rect.x = random.randint(200, 600)
# Classe do barco
class Barco(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = barco_sprite_img  # sprite carregado
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT - 100))
        self.speed = 3
        self.carga = 0
        self.max_carga = 100

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed


        if self.rect.left < 200:
            self.rect.left = 200
        if self.rect.right > 600:
            self.rect.right = 600

    def voltar_ao_porto(self):
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 100)
        self.carga = 0


#
# Variáveis de controle
#
nivel = 1
caminhao_group = pygame.sprite.Group()
em_descarga = False
tempo_descarga = 0
Vida = 5

# Criar Caminhao iniciais
for _ in range(qtd_caminhao):
    x = random.randint(200, 600)
    y = random.randint(-100, -10)
    caminhao_group.add(Caminhao(x, y,any,3, 6))

# Instanciar o barco
barco = Barco()

#
# Loop principal do jogo
#
running = True
while running:
    clock.tick(60)  # 60 frames por segundo

    # Processar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Se o barco estiver carregando até o limite, inicia o descarregamento
    if not em_descarga and barco.carga >= barco.max_carga:
        som_aviso.play()

        # Cria uma lista das Caminhao no céu (fora do alcance do barco)
        Caminhao_estrada = [m for m in caminhao_group if m.rect.y < HEIGHT / 2]
        while Caminhao_estrada:
            rem = Caminhao_estrada.pop()
            caminhao_group.remove(rem)


        em_descarga = True
        tempo_descarga = pygame.time.get_ticks()

    if em_descarga:
        # O barco volta ao porto para descarregar
        barco.voltar_ao_porto()
        # Aguarda 2 segundos para descarregar
        if pygame.time.get_ticks() - tempo_descarga > 2000:
            barco.carga = 0
            em_descarga = False
        continue  # pula o restante do loop enquanto descarrega

    # Atualiza movimento do barco
    barco.update(keys)
    caminhao_group.update()


    # Detecta colisões entre o barco e as Caminhao
    colisoes = pygame.sprite.spritecollide(barco, caminhao_group, True)
    for caminhao in colisoes:
        Vida -= 1


    # Garantir que o número de Caminhao esteja constante
    while len(caminhao_group) < qtd_caminhao:
        x = random.randint(0, WIDTH - 20)
        y = random.randint(-100, -10)
        caminhao_group.add(Caminhao(x, y,any,v_min,v_max))

    #
    # Desenhar a tela
    #
    screen.blit(background_img, (0, 0))
    # Pode adicionar desenho do porto se desejar
    # screen.blit(port_sprite, port_rect) # nao esquecer de carregar a imagem e criar o rect
    score_text = f"Vida: {Vida}"
    score_surface = FONT.render(score_text, True, (255, 255, 255))
    screen.blit(score_surface, (10, 80))
    caminhao_group.draw(screen)
    screen.blit(barco.image, barco.rect)

    # Mostrar quantidade de Caminhao capturadas
    info_text = f'Moedas: {barco.carga}/{barco.max_carga}'
    nivel_text = f'Nível: {nivel}'
    screen.blit(FONT.render(info_text, True, (255, 255, 255)), (10, 10))
    screen.blit(FONT.render(nivel_text, True, (255, 255, 255)), (10, 50))

    # Se desejar, pode aqui aumentar o nível
    if barco.carga >= barco.max_carga:
        nivel += 1
        if nivel > 3:
            nivel = 3  # máximo nível
        qtd_caminhao, v_min, v_max = configurar_dificuldade(nivel)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o pygame ao sair do loop
pygame.quit()
sys.exit()
