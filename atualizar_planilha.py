import subprocess
import sys

from precos import carregar_precos, salvar_precos


def escolher_ingrediente(ingredientes):
    chaves = list(ingredientes.keys())
    print("\nEscolha qual ingrediente mudou de preço no mercado:")
    for i, chave in enumerate(chaves, start=1):
        print(f"  [{i}] {ingredientes[chave]['nome']}")

    opcao = input("\nDigite o NÚMERO do item e aperte ENTER: ")
    if not opcao.isdigit() or not (1 <= int(opcao) <= len(chaves)):
        print("Opção inválida. Saindo sem alterar nada...")
        sys.exit()
    return chaves[int(opcao) - 1]


def main():
    print("=" * 55)
    print(" 🍰 ATUALIZADOR AUTOMÁTICO DE PREÇOS ")
    print("=" * 55)

    ingredientes = carregar_precos()
    chave = escolher_ingrediente(ingredientes)
    item = ingredientes[chave]

    print(f"\n-> O preço atual de '{item['nome']}' é: R$ {item['preco']:.2f}")

    entrada = input("Digite o NOVO PREÇO pago no mercado (ex: 6.50): ").replace(",", ".")
    try:
        novo_preco = float(entrada)
    except ValueError:
        print("❌ Valor inválido! Digite apenas números (ex: 6.50).")
        return

    item["preco"] = novo_preco
    salvar_precos(ingredientes)
    print(f"\n✅ SUCESSO! O preço de '{item['nome']}' foi atualizado para R$ {novo_preco:.2f} em precos.json!")
    print("💡 Como todos os outros scripts leem o preço daqui, o Custo do Bolo e o Lucro em qualquer")
    print("   planilha/relatório gerado a partir de agora já vão sair recalculados com esse valor.")

    resposta = input("\nQuer regenerar as planilhas (.xlsx) agora com o preço novo? (s/n): ").strip().lower()
    if resposta == "s":
        subprocess.run([sys.executable, "gerar_planilha.py"])
        subprocess.run([sys.executable, "gerar_dashboard.py"])
        print("\n💡 Planilhas regeneradas com o novo preço!")
    else:
        print("\n💡 Lembre-se de rodar 'python gerar_planilha.py' e 'python gerar_dashboard.py' quando quiser")
        print("   aplicar esse novo preço nos arquivos .xlsx.")


if __name__ == "__main__":
    main()