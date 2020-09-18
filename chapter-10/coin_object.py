import coin_class

def main():
    my_coin = coin_class.Coin()

    print('This side is up', my_coin.get_sideup())

    #Toss the coin
    my_coin.toss()
    print('Now this side is up', my_coin.get_sideup())

main()
