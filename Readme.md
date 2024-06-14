# Prova 2

## Respostas para as perguntas técnicas

1. Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.

R: O método de detecção escolhido para realizar a atividade foi o Haar Cascade, que é um algoritmo de detecção de objetos. Seu funcionamento se baseia em criar imagens integrais que permitem o cálculo mais rápido dos recursos de Haar, uma vez que não precisa passar por cada pixel. Após isso, é utilizado o algoritmo Adaboost para escolher os melhores recursos e treinar os classificadores com base nisso. Depois, é realizado a cascata de classificadores que processam a imagem em etapas e consegue identificar regiões com detecções positivas ou negativas e realizar a identificação do objeto.

2. Considere as seguintes alternativas para resolver o problema de detecção de faces:

- HAAR Cascade
- CNN
- NN Linear
- Filtros de correlação cruzada

Classifique-os (coloque em ordem) em termos de viabilidade técnica (se é possível resolver o problema), facilidade de implementação e versatilidade da solução. Justifique sua classificação.

R: A ordem escolhida foi:

1º Haar Cascade - além de conseguir resolver o problema com boa precisão dependendo da forma como for treinado e da quantidade de cascatas, sua execução consegue ser relativamente rápida em comparação com outros algoritmos de detecção de objeto, além de apresentar uma implementação mais fácil.
2º CNN -  um algoritmo de rede neural convolucional também consegue resolver o problema e de forma muito eficiente, uma vez que é um algoritmo robusto na forma que atua, porém ele performa com um pouco mais de custo operacional ao se comparar com o Haar Cascade o que pode tornar a aplicação mais lenta ao ser aplicado a um vídeo.
3º Filtros de correlação cruzada - a partir dos filtros de correlação cruzada também seria possível resolver o problema em questão e com certa precisão, porém, ao realiar a correlação cruzada seria muito custoso para o processamento de vários frames, e não seria o método mais viável para o problema em questão. 
4º NN Linear

3.Considerando as mesmas alternativas acima, faça uma nova classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face.

1º Haar Cascade - possui métodos para encontrar isso de forma eficaz a partir do terinamento que for feito.
2º Filtros de correlação cruzada- pois seria mais preciso para detectar emoções através de comparações 
3º CNN- possui métodos para encontrar isso de forma eficaz a partir do treinamento que for feito, mas pode ser mais custoso operacionalmente e não ter um desempenho tão bom quanto os dois primeiros. lugares
4º NN Linear

4. A solução apresentada ou qualquer outra das que foram listadas na questão 2. tem a capacidade de considerar variações de um frame para outro (e.g. perceber que em um frame a pessoa está feliz e isso influenciar na detecção do próximo frame)? Se não, quais alterações poderiam ser feitas para que isso seja possível?

Acredito que, adicionando aplicando e ajustado osistema de filtros de correlação cruzada para o problema em específico, seria possível aplicar uma comparação entre diferentes frames, fazendo com que isso fosse utilizado para influenciar durante a análise do frame seguinte. Isso porque o algoritmo de correlação cruzada é muito eficiente em avalizar  dois frames diferentes em dectar padrões e similaridades, e, a partir diss  seria possível não só dectar os padrões de feição para emoções diferentes.

## Como rodar a solução desenvolvida

Primeiro, é necessário clonar o seguinte repositório do github. Uma explicação mais clara de como fazer isso está presente no seguinte [link](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository)

Para executar a solução, é necessário:

1. Ter o Python instalado
2. Instalar o OpenCv2. Para isso, vá no terminal do repositorio e execute `pip install opencv-python`
3. Ir até a pasta correspondente: `cd prova2_mod6/projeto_prova`
4. Rodar o arquivo: `python identify_faces.py`

[Vídeo da solução](https://drive.google.com/file/d/1uPIJxJNO0SrmhFuyL_sbxC0tSDLf377r/view?usp=sharing)