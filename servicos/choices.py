from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "Trocar válvula do motor"
    TROCAR_OLEO = "TO", "Troca de óleo"
    BALANCEAMENTO = "B", "Balanceamento"
    ALINHAMENTO = "AL", "Alinhamento"
    FREIOS = "FR", "Revisão de freios"
    ARREFECIMENTO = "AR", "Sistema de arrefecimento"
    SUSPENSAO = "SU", "Suspensão"
    EMBREAGEM = "EM", "Embreagem"
    DIRECAO = "DI", "Direção"
    ELETRICA = "EL", "Elétrica"
    TRANSMISSAO = "TR", "Transmissão"
    PNEUS = "PN", "Pneus"
    ESCAPAMENTO = "ES", "Escapamento"
