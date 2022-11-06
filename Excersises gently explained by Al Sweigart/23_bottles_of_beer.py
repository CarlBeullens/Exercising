
for i in range(99, 0, -1):
    
    if not i == 1:
        stanza = (f"{i} bottles of beer on the wall,\n"
                f"{i} bottles of beer,\n"
                f"Take one down,\n"
                f"Pass it around,\n"
                f"{i - 1} bottles of beer on the wall,\n"
                )
    else:
        stanza = (f"{i} bottle of beer on the wall,\n"
                f"{i} bottle of beer,\n"
                f"Take one down,\n"
                f"Pass it around,\n"
                f"No more bottles of beer on the wall!\n"
                )
    
    print(stanza)