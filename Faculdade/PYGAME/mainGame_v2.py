from random import choice

import pygame
import random
import sys

pygame.init()


# Configurações
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)

som_caminhao = pygame.mixer.Sound(r'./Assets2/Sounds/PassBy.mp3')
som_buzina_2 =pygame.mixer.Sound(r'./Assets2/Sounds/Truck-Horn.mp3')
som_buzina_1 = pygame.mixer.Sound (r'./Assets2/Sounds/Truck-Horn 2.mp3')
som_batida =pygame.mixer.Sound(r'./Assets2/Sounds/Crash 1.mp3')
som_batida_2 =pygame.mixer.Sound(r'./Assets2/Sounds/Crash 2.mp3')

som_caminhao.set_volume(0.2)
som_buzina_2.set_volume(0.2)
som_buzina_1.set_volume(0.2)
som_batida.set_volume(0.2)
som_batida_2.set_volume(0.2)

pygame.mixer.set_num_channels(20)
canal_spawn = pygame.mixer.Channel(1)
canal_batida = pygame.mixer.Channel(2)
canal_buzina =pygame.mixer.Channel(3)

buzina = [som_buzina_1, som_buzina_2]
batida = [som_batida, som_batida_2]

qtd_caminhao = 2

# Fundo
background_img = pygame.image.load(r'./Assets2/Road/Road_00.png')
background_img = pygame.transform.scale(background_img, (HEIGHT, background_img.get_height()))
background_img = pygame.transform.scale(background_img, (WIDTH, background_img.get_width()))
background_img = pygame.transform.rotate(background_img, 90)

# Barco
barco_sprite_img = pygame.image.load(r'./Assets2/Fusca.png').convert_alpha()
barco_sprite_img = pygame.transform.smoothscale(barco_sprite_img, (54*1.25, 85*1.25))

def configurar_dificuldade(nivel):
    qtd_caminhao = 2
    if nivel == 1:
        v_min, v_max = 7, 9
    else:
        v_min = 7 + nivel * 1.5
        v_max = 9 + nivel * 1.5
    return qtd_caminhao, v_min, v_max

# Controle de faixas
FAIXAS_X = [180, 340, 500]
faixas_ocupadas = set()

nivel = 1
qtd_caminhao    ,v_min, v_max = configurar_dificuldade(nivel)
inicio_tempo_nivel = pygame.time.get_ticks()
inicio_tempo_geral = pygame.time.get_ticks()
Vida = 5

class Caminhao(pygame.sprite.Sprite):
    def __init__(self, x, y, tipo, v_min, v_max):
        if nivel == 1:
            v_min= 7
            v_max= 9
        if nivel > 1:
            v_min =int( 7 + nivel )
            v_max =int( 9 + nivel )


        super().__init__()
        self.image = pygame.image.load(r'./Assets2/Caminhao.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (57*2, 86*2))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.randint(v_min, v_max)
        self.faixa_x = x
        self.faixa_y= y

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            faixas_ocupadas.discard(self.faixa_x)
            

            faixa_disponivel = list(set(FAIXAS_X) - faixas_ocupadas)
            if faixa_disponivel:
                nova_faixa = random.choice(faixa_disponivel)
            else:
                nova_faixa = self.faixa_x

            self.rect.x = nova_faixa
            self.faixa_x = nova_faixa
            self.rect.y = random.randint(-100, -10)
            self.speed = random.randint(int(7 + nivel), int(9 + nivel))  # atualiza velocidade
            faixas_ocupadas.add(nova_faixa)
            canal_spawn.play(som_caminhao)
            canal_buzina.play(random.choice(buzina))
            


class Barco(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = barco_sprite_img
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT - 100))
        self.carga = 0
        self.max_carga = 100
        if nivel == 1:
            self.speed = 9
        if nivel > 1:
            self.speed=int(7+nivel)

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
    canal_spawn.play(som_caminhao)
    canal_buzina.play(random.choice(buzina))


caminhao_group = pygame.sprite.Group()
barco = Barco()




running = True
while running:
    clock.tick(60)

    # Subir nível a cada 30 segundos
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - inicio_tempo_nivel >= 10000:
        nivel += 1
        Vida += 1
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
        canal_batida.play(random.choice(batida))
        if caminhao.faixa_x in faixas_ocupadas:
            faixas_ocupadas.remove(caminhao.faixa_x)

    if Vida <= 0:
        # opcional: desenha “Game Over” antes de sair
        game_over_surf = FONT.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_surf, (WIDTH // 2 - game_over_surf.get_width() // 2,
                                     HEIGHT // 2 - game_over_surf.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(3000)  # espera 2 segundos
        running = False
        continue  # pula resto do loop para sair imediatamente

    if len(caminhao_group) < qtd_caminhao:
        spawn_caminhao()

    screen.blit(background_img, (0, 0))
    screen.blit(barco.image, barco.rect)
    caminhao_group.draw(screen)

    vida_text = FONT.render(f"Vida: {Vida}", True, (255, 255, 255))
    nivel_text = FONT.render(f"Nível: {nivel}", True, (255, 255, 255))

    screen.blit(vida_text, (10, 80))
    screen.blit(nivel_text, (10, 50))
    screen.blit(tempo_surface, (10, 110))  # mostra o tempo no canto

    mensagem = "Desvie dos caminhões!"
    texto_direita = FONT.render(mensagem, True, (255, 255, 0))  # cor amarela
    pos_x = WIDTH - texto_direita.get_width() - 10
    pos_y = 10
    screen.blit(texto_direita, (pos_x, pos_y))

    if tempo_segundos < 10:
        mensagem = "Use as setas para se movimentar"
        texto_direita = FONT.render(mensagem, True, (255, 255, 0))  # cor amarela
        pos_x = WIDTH - texto_direita.get_width() - 10
        pos_y = 40
        screen.blit(texto_direita, (pos_x, pos_y))

        mensagem = "A cada 10 segs o jogo fica mais dificil"
        texto_direita = FONT.render(mensagem, True, (255, 255, 0))  # cor amarela
        pos_x = WIDTH - texto_direita.get_width() - 10
        pos_y = 70
        screen.blit(texto_direita, (pos_x, pos_y))
    

    

    pygame.display.flip()

pygame.quit()
sys.exit()