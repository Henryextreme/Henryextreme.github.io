# ... (tudo igual até a classe Caminhao)

class Caminhao(pygame.sprite.Sprite):
    def __init__(self, x, y, tipo, v_min, v_max):
        super().__init__()
        self.image = pygame.image.load('CatchTheCoin\\Assets2\\Caminhao.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (57*2, 86*2))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.randint(v_min, v_max)
        self.faixa_x = x

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            liberar_faixa(self)
            faixa_disponivel = list(set(FAIXAS_X) - faixas_ocupadas)
            if faixa_disponivel:
                nova_faixa = random.choice(faixa_disponivel)
                faixas_ocupadas.add(nova_faixa)
                self.faixa_x = nova_faixa
                self.rect.x = nova_faixa
            else:
                # Se não tiver faixa disponível, mantém posição x atual
                self.rect.x = self.faixa_x
            self.rect.y = random.randint(-100, -10)

def liberar_faixa(caminhao):
    if caminhao.faixa_x in faixas_ocupadas:
        faixas_ocupadas.remove(caminhao.faixa_x)

def spawn_caminhao():
    faixa_disponivel = list(set(FAIXAS_X) - faixas_ocupadas)
    if not faixa_disponivel:
        return None
    x = random.choice(faixa_disponivel)
    faixas_ocupadas.add(x)
    y = random.randint(-100, -10)
    novo = Caminhao(x, y, any, v_min, v_max)
    caminhao_group.add(novo)
    return novo

# No loop principal, na colisão:
colisoes = pygame.sprite.spritecollide(barco, caminhao_group, True)
for caminhao in colisoes:
    Vida -= 1
    liberar_faixa(caminhao)

# Na hora de garantir qtd caminhões:
while len(caminhao_group) < qtd_caminhao:
    spawn_caminhao()

