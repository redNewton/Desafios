while True: 
    try: 
          perna = input()
           
          if (perna == 'esquerda'):
             print('ingles')
            
          if (perna == 'direita'):
             print('frances')
             
          if (perna == 'nenhuma'):
             print('portugues')
             
          if (perna == 'ambas'):
             print('caiu')
             
    except EOFError: 
        break
