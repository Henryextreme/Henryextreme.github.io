import pygame
import random
import sys

pygame.init()

# Sons
som_aviso = pygame.mixer.Sound(r'CatchTheCoin\Assets/Audio/notificacao.mp3')
som_beep = pygame.mixer.Sound(r'CatchTheCoin\Assets/Audio/beep.mp3')

# Configurações
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)

# Fundo
background_img = pygame.image.load(r'CatchTheCoin\Assets2\Road\Road_00.png')
background_img = pygame.transform.scale(background_img, (HEIGHT, background_img.get_height()))
background_img = pygame.transform.scale(background_img, (WIDTH, background_img.get_width()))
background_img = pygame.transform.rotate(background_img, 90)

# Barco
barco_sprite_img = pygame.image.load(r'CatchTheCoin/Assets2/Fusca.png').convert_alpha()
barco_sprite_img = pygame.transform.smoothscale(barco_sprite_img, (54*1.25, 85*1.25))

def configurar_dificuldade(nivel):
    if nivel == 1:
        return 2, 3, 4
    elif nivel == 2:
        return 3, 4, 6
    elif nivel == 3:
        return 4, 5, 7
    else:
        return 2, 3, 4

# Controle de faixas
FAIXAS_X = [200, 400, 600]
faixas_ocupadas = set()

nivel = 1
qtd_caminhao, v_min, v_max = configurar_dificuldade(nivel)
inicio_tempo_nivel = pygame.time.get_ticks()
inicio_tempo_geral = pygame.time.get_ticks()
Vida = 5

class Caminhao(pygame.sprite.Sprite):
    def __init__(self, x, y, tipo, v_min, v_max):
        super().__init__()
        self.image = pygame.image.load('CatchTheCoin\Assets2\Caminhao.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (57*2, 86*2))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.randint(v_min, v_max)
        self.faixa_x = x

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            if self.faixa_x in faixas_ocupadas:
                faixas_ocupadas.remove(self.faixa_x)
            faixa_disponivel = list(set(FAIXAS_X) - faixas_ocupadas)
            if faixa_disponivel:
                nova_faixa = random.choice(faixa_disponivel)
                faixas_ocupadas.add(nova_faixa)
                self.faixa_x = nova_faixa
                self.rect.x = nova_faixa
            else:
                self.rect.x = self.faixa_x
            self.rect.y = random.randint(-100, -10)

class Barco(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = barco_sprite_img
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

def spawn_caminhao():
    faixa_disponivel = list(set(FAIXAS_X) - faixas_ocupadas)
    if not faixa_disponivel:
        return
    x = random.choice(faixa_disponivel)
    faixas_ocupadas.add(x)
    y = random.randint(-100, -10)
    caminhao_group.add(Caminhao(x, y, any, v_min, v_max))

caminhao_group = pygame.sprite.Group()
barco = Barco()

for _ in range(qtd_caminhao):
    spawn_caminhao()

running = True
while running:
    clock.tick(60)

    # Subir nível a cada 30 segundos
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - inicio_tempo_nivel >= 30000:
        nivel += 1
        if nivel > 3:
            nivel = 3
        qtd_caminhao, v_min, v_max = configurar_dificuldade(nivel)
        inicio_tempo_nivel = tempo_atual

    # Tempo total decorrido para mostrar na tela
    tempo_decorrido_ms = tempo_atual - inicio_tempo_geral
    tempo_segundos = tempo_decorrido_ms // 1000
    minutos = tempo_segundos // 60
    segundos = tempo_segundos % 60
    tempo_formatado = f"Tempo: {minutos:02d}:{segundos:02d}"
    tempo_surface = FONT.render(tempo_formatado, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    barco.update(keys)
    caminhao_group.update()

    # Colisões
    colisoes = pygame.sprite.spritecollide(barco, caminhao_group, True)
    for caminhao in colisoes:
        Vida -= 1
        if caminhao.faixa_x in faixas_ocupadas:
            faixas_ocupadas.remove(caminhao.faixa_x)

    while len(caminhao_group) < qtd_caminhao:
        spawn_caminhao()

    screen.blit(background_img, (0, 0))
    screen.blit(barco.image, barco.rect)
    caminhao_group.draw(screen)

    vida_text = FONT.render(f"Vida: {Vida}", True, (255, 255, 255))
    nivel_text = FONT.render(f"Nível: {nivel}", True, (255, 255, 255))

    screen.blit(vida_text, (10, 80))
    screen.blit(nivel_text, (10, 50))
    screen.blit(tempo_surface, (10, 110))  # mostra o tempo no canto

    pygame.display.flip()

pygame.quit()
sys.exit()
