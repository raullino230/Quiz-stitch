import os
from fasthtml.common import fast_app, serve, Title, Main, Link
from componentes import (
    gerar_hearder,
    gerar_perguntas,
    gerar_tabela_pontuação,
    gerar_respostas,
    gerar_footer
)

_app, route = fast_app(
    pico=False,
    secret_key=os.environ.get("SECRET_KEY", "chave-local-de-desenvolvimento"),
    hdrs=(Link(rel="stylesheet", href="/static/style.css"),)
      Meta(
            name="google-site-verification",
            content="9eUI0pLtQ8XsvgcETjFVmWNogTGGGNT_QQtvi_J37bQ"
        )
)

app = _app


@route("/")
def pagina_principal():
    formulario_perguntas = gerar_perguntas()
    Table_de_pontuação = gerar_tabela_pontuação()
    Formulario_respostas = gerar_respostas()

    return Title("Quiz sobre o stitch"), Main(
        gerar_hearder("Esse quiz foi desenvolvido especialmente para minha irmã, Livia!!!"),
        formulario_perguntas,
        Table_de_pontuação,
        Formulario_respostas,
        gerar_footer()
    )


if __name__ == "__main__":
    serve()