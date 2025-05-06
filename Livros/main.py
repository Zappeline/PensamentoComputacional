from models.Livros import Livros

chorao = Livros(titulo="Se não eu, quem vai fazer você feliz?", autor=" Graziela Gonçalves", ano_publicado=2018, num_pag=43, pag_atual=1)

chorao.mostrar_infos()
chorao.avancar_pag()
chorao.avancar_pag()
chorao.avancar_pag()
chorao.avancar_pag()
chorao.avancar_pag()
chorao.voltar_pag()

print("VocÊ está na pagina:", chorao.pag_atual,"de um total de:", chorao.num_pag, "páginas.")


