pokemon = {
    "pikachu" : '''Pikachu are a species of Pokémon, fictional creatures that
appear in an assortment of video games, animated television 
shows and movies, trading card games, and comic books 
licensed by The Pokémon Company, a Japanese corporation. 
They are yellow rodent-like creatures with powerful 
electrical abilities. ''',

    "raichu" : '''raichu has a regional variant that is Electric/Psychic. 
It evolves from Pikachu when exposed to a Thunder Stone.
All Pikachu in Alola will evolve into this form regardless
of their origin.''',
    "onix" : '''Onix resembles a giant chain of gray boulders that become 
smaller towards the tail. It has a rocky spine on its head
and a pair of black eyes right beneath it. This Pokémon has 
a magnet in its brain that serves as an internal compass. 
Its body absorbs many hard objects, making its body very 
solid. As it grows older, it becomes more rounded and 
smoother, eventually becoming similar to black diamonds.'''
}


while True:   
    n = input("Nhập tên pokemon cần tìm:")    
    for key, value in pokemon.items():
        if n.lower() == key:
            print(value)




