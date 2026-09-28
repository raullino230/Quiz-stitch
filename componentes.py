from fasthtml.common import *

def gerar_hearder(paragrafo):
    return Header(
        H1("Quiz sobre o Stitch"),
        P(paragrafo, cls="subtitulo")
    )

def gerar_perguntas():
    formulario_perguntas = Main(
     Section(
        H2("1.Quem é o Stitch?", name = "p1"),
        Form(
            Input(type = "checkbox", id = "p1a", name = "P1a_stitch"),
            Label("Um cachorro comum", _for = "p1a"),Br(),

            Input(type = "checkbox", id = "p1b", name = "P1b_stitch"),
            Label("Um experimento alienígena", _for = "p1b"),Br(),

            Input(type = "checkbox", id = "p1c", name = "P1c_stitch"),
            Label("Um robô", _for = "p1c"),Br(),

            Input(type = "checkbox", id = "p1d", name = "P1d_stitch"),
            Label("Um super-herói", _for = "p1d"),Br(),                     
            cls = "opcoes"
        ),
        cls = "pergunta"
     ),
    Br(),
    
    Section(
        H2("2.Qual é o nome verdadeiro de Stitch?", name = "p2"),
        Form(
            Input(type = "checkbox", id = "p2a", name = "P2a_stitch"),
            Label("Experimento 625", _for = "p2a"),Br(),

            Input(type = "checkbox", id = "p2b", name = "P2b_stitch"),
            Label("Experimento 626", _for = "p2b"),Br(),

            Input(type = "checkbox", id = "p2c", name = "P2c_stitch"),
            Label("Experimento 626-B", _for = "p2c"),Br(),

            Input(type = "checkbox", id = "p2d", name = "P2d_stitch"),
            Label("Experimento 600", _for = "p2d"),Br(),
            cls = "opcoes"
        ),
        cls = "pergunta"
    ),
    Br(),

    Section(
        H2("3. Quem criou Stitch?", name = "p3"),
        Form(
            Input(type = "checkbox", id = "p3a", name = "P3a_stitch"),
            Label("Jumba", _for = "p3a"),Br(),

            Input(type = "checkbox", id = "p3b", name = "P3b_stitch"),
            Label("Gantu", _for = "p3b"),Br(),

            Input(type = "checkbox", id = "p3c", name = "P3c_stitch"),
            Label("Pleakley", _for = "p3c"),Br(),

            Input(type = "checkbox", id = "p3d", name = "P3d_stitch"),
            Label("Cobra Bubbles", _for = "p3d"),Br(),           
            cls = "opcoes"
        ),
        cls = "pergunta"
    ),
    Br(),

    Section(
        H2("4. Quem cuida de Stitch e faz parte da família dele?", name = "p4"),
        Form(
            Input(type = "checkbox", id = "p4a", name = "P4a_stitch"),
            Label("Lilo", _for = "p4a"),Br(),

            Input(type = "checkbox", id = "p4b", name = "P4b_stitch"),
            Label("Nani", _for = "p4b"),Br(),

            Input(type = "checkbox", id = "p4c", name = "P4c_stitch"),
            Label("Angel", _for = "p4c"),Br(),

            Input(type = "checkbox", id = "p4d", name = "P4d_stitch"),
            Label("Moana", _for = "p4d"),Br(),            
            cls = "opcoes"
        ),
        cls = "pergunta"
    ),
    Br(),

    Section(
        H2("5. Onde Lilo e Stitch vivem?", name = "p5"),
        Form(
            Input(type = "checkbox", id = "p5a", name = "P5a_stitch"),
            Label("Califórnia", _for = "p5a"),Br(),

            Input(type = "checkbox", id = "p5b", name = "P5b_stitch"),
            Label("Havaí", _for = "p5b"),Br(),

            Input(type = "checkbox", id = "p5c", name = "P5c_stitch"),
            Label("Nova York", _for = "p5c"),Br(),

            Input(type = "checkbox", id = "p5d", name = "P5d_stitch"),
            Label("Tóquio", _for = "p5d"),Br(),       
            cls = "opcoes"
        ),
        cls = "pergunta"
    ),
    Br(),

    Section(
        H2("6. Qual é uma das principais características de Stitch?", name = "p6"),
        Form(
            Input(type = "checkbox", id = "p6a", name = "P6a_stitch"),
            Label("É extremamente poderoso e inteligente", _for = "p6a"),Br(),

            Input(type = "checkbox", id = "p6b", name = "P6b_stitch"),
            Label("Não gosta de música", _for = "p6b"),Br(),

            Input(type = "checkbox", id = "p6c", name = "P6c_stitch"),
            Label("É um alienígena criado para causar destruição", _for = "p6c"),Br(),

            Input(type = "checkbox", id = "p6d", name = "P6d_stitch"),
            Label("É um humano com superpoderes", _for = "p6d"),Br(),
            cls = "opcoes"
        ),
        cls = "pergunta"
    ),
    Br(),

    Section(
        H2("7. Por que Stitch foi criado?", name = "p7"),
        Form(
            Input(type = "checkbox", id = "p7a", name = "P7a_stitch"),
            Label("Para ajudar humanos", _for = "p7a"),Br(),

            Input(type = "checkbox", id = "p7b", name = "P7b_stitch"),
            Label("Para ser um animal de estimação", _for = "p7b"),Br(),

            Input(type = "checkbox", id = "p7c", name = "P7c_stitch"),
            Label("Para causar destruição e criar confusão", _for = "p7c"),Br(),

            Input(type = "checkbox", id = "p7d", name = "P7d_stitch"),
            Label("Para proteger a Terra", _for = "p7d"),Br(),
            cls = "opcoes"
        ),
        cls = "pergunta"
    ),Br(),

    Section(
        H2("8. 🖼️ Quem é o personagem mostrado na imagem abaixo?", name = "p8"),
        Figure(
            Img(src = "/img/Pleakley.webp", alt = "Um personagem de Stitch!", cls = "imagem-personagem")
        , cls = "figura-pergunta"),Br(),
        Form(
            Input(type = "checkbox", id = "p8a", name = "P8a_stitch"),
            Label("Stitch", _for = "p8a"),Br(),

            Input(type = "checkbox", id = "p8b", name = "P8b_stitch"),
            Label("Jumba", _for = "p8b"),Br(),

            Input(type = "checkbox", id = "p8c", name = "P8c_stitch"),
            Label("Gantu", _for = "p8c"),Br(),

            Input(type = "checkbox", id = "p8d", name = "P8d_stitch"),
            Label("Pleakley", _for = "p8d"),Br(),
            cls = "opcoes"
        ),
        cls = "pergunta"
    ),
    Br(),

    Section(
        H2("9.✍️ Escreva: Qual é o significado da palavra ", Strong("Ohana"), " na história de Lilo & Stitch?", name = "p9"),

        Form(
            Input(type = "text", id = "p9t", Placeholder = "Digite sua resposta...", cls = "resposta-texto")
        , cls = "opcoes"),
        cls = "pergunta"
    ),
    Br(),

    Section(
        H2("10. O que Stitch aprende durante a história?", name = "p10"),

        Form(
            Input(type = "checkbox", id = "p10a", name = "P10a_stitch"),
            Label("Que precisa voltar para seu planeta", _for = "p10a"),Br(),
        
            Input(type = "checkbox", id = "p10b", name = "P10b_stitch"),
            Label("Que dinheiro é o mais importante", _for = "p10b"),Br(),

            Input(type = "checkbox", id = "p10c", name = "P10c_stitch"),
            Label("O significado de família e de pertencer a um grupo", _for = "p10c"),Br(),

            Input(type = "checkbox", id = "p10d", name = "P10d_stitch"),
            Label("Que não precisa de ninguém", _for = "p10d"),Br(),
            cls = "opcoes"
        ),
        cls = "pergunta"
    )
    , cls = "quiz-perguntas"), Br(),
    return formulario_perguntas

def gerar_tabela_pontuação():
    Table_de_pontuação = Section(
        H2("Tabela de pontuação", name = "Tabela pontuação"),
        Table(
            Thead(
                Tr(
                    Th("Pontuação"),
                    Th("Avaliação"),
                )
            ),
            Tbody(
                Tr(
                    Td("Acertou: 0-3"),
                    Td("🌱 Precisa estudar mais sobre Stitch"),
                ),
                Tr(
                    Td("Acertou: 4-6"),
                    Td("🙂 Você conhece um pouco o Stitch"),
                ),
                Tr(
                    Td("Acertou: 7-8"),
                    Td("😎 Você conhece bastante o Stitch"),
                ),
                Tr(
                    Td("Acertou: 9-10"),
                    Td("🏆 Você é um verdadeiro fã de Stitch!"),
                ),
                
            ),
            Tfoot(
                Tr(
                    Td("Agradecimentos: 🎉 Muito bem! Você foi incrível! 🥰 Continue aprendendo e se divertindo com o Stitch para ficar ainda melhor! 💙🌺", colspan = "2")
                )
            ),
            cls = "tabela"
        ),
        cls = "tabela-pontuacao"
    ), Br()
    return Table_de_pontuação

def gerar_respostas():
    Formulario_repostas = Section(
        H2("Verifique suas respostas!", name = "Verifique respostas"),
        Details(
            Summary("Clique aqui para ver as respostas do quiz!"),
            Ol(
                Li(" Um experimento alienígena"),
                Li(" Experimento 626"),
                Li(" Jumba"),
                Li(" Lilo e Nani"),
                Li(" Havaí"),
                Li(" É um alienígena criado para causar destruição"),
                Li(" Para causar destruição e criar confusão"),
                Li(" Pleakley"),
                Li(" Ohana significa família"),
                Li(" O significado de família e de pertencer a um grupo"),
                cls = "lista-respostas"
            ),
            cls = "respostas-details"
        ),
        cls = "respostas"
    ),Br()
    return Formulario_repostas

def gerar_footer():
    return Footer(
        P("© Quiz do stitch. Todos os direitos reservados.", cls = "footer-copyright"),
        P("Esse quiz foi feito com muito amor e carinho para minha irmã, Livia!! 💙🌺", cls = "footer-mensagem")
    )