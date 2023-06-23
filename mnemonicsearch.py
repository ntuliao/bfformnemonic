from mnemonic import Mnemonic
from hdwallet import HDWallet
from hdwallet.symbols import BTC
import threading
import secp256k1
from bloomfilter import BloomFilter
import multiprocessing
#from numba import jit
print("Random Generation inclusive CheckSum Check")

# Load Bitcoin addresses from bloom file
with open("btc.bf", "rb") as fp:
    btc_bloom = BloomFilter.load(fp)
addr_count_btc = len(btc_bloom)
print('Total Bitcoin addresses Loaded from Bloomfile: ', str(addr_count_btc))

# Load Litecoin addresses from bloom file
#with open("ltc.bf", "rb") as fp:
 #   ltc_bloom = BloomFilter.load(fp)
#addr_count_ltc = len(ltc_bloom)
#print('Total Litecoin addresses Loaded from Bloomfile: ', str(addr_count_ltc))

# Load Ethereum addresses from bloom file
#with open("eth.bf", "rb") as fp:
 #   eth_bloom = BloomFilter.load(fp)
#addr_count_eth = len(eth_bloom)
#print('Total Ethereum addresses Loaded from Bloomfile: ', str(addr_count_eth))

# Load Dash addresses from bloom file
#with open("dash.bf", "rb") as fp:
  #  dash_bloom = BloomFilter.load(fp)
#addr_count_dash = len(dash_bloom)
#print('Total Dash addresses Loaded from Bloomfile: ', str(addr_count_dash))

# Load Dogecoin addresses from bloom file
#with open("doge.bf", "rb") as fp:
  #  doge_bloom = BloomFilter.load(fp)
#addr_count_doge = len(doge_bloom)
#print('Total Dogecoin addresses Loaded from Bloomfile: ', str(addr_count_doge))

#@jit
def search(words, mnemo, allowed_strengths):
    for strength in allowed_strengths:
        for p in range(0, 10):
            mnemo = Mnemonic(language)
            words = mnemo.generate(strength=strength)
            hdwallet = HDWallet(symbol=BTC)
            wallet = hdwallet.from_mnemonic(words)
            path = hdwallet.from_path(path="m/44'/0'/0'/0/" + str(p))
            priv = hdwallet.private_key()
            privkey = int(priv, base=16)
            add1 = secp256k1.privatekey_to_address(0, True, privkey)
            add2 = secp256k1.privatekey_to_address(0, False, privkey)
            add3 = secp256k1.privatekey_to_address(1, True, privkey)
            add4 = secp256k1.privatekey_to_address(2, True, privkey)
            found = False

            if add1 in btc_bloom or add2 in btc_bloom or add3 in btc_bloom or add4 in btc_bloom:
                print("BTC MATCH FOUND!!!")
                print("Words: ", words)
                print("--------------------")
                print("BTC Compressed: ", add1)
                print("BTC Uncompressed: ", add2)
                print("BTC Segwit: ", add3)
                print("BTC Bech31: ", add4)
                print("--------------------")
                with open("found.txt", "a") as f:
                    f.write(f"BTC Winner!!!\n")
                    f.write(f"Mnemonic: {words}\n")
                    f.write(f"BTC Compressed: {add1}\n")
                    f.write(f"BTC Uncompressed: {add2}\n")
                    f.write(f"BTC Segwit: {add3}\n")
                    f.write(f"BTC Bech31: {add4}\n")
                found = True

#         // """  if add1 in ltc_bloom or add2 in ltc_bloom or add3 in ltc_bloom or add4 in ltc_bloom:
  #              print("LTC MATCH FOUND!!!")
    #            print("Words: ", words)
      #          print("--------------------")
        #        print("LTC Compressed: ", add1)
          #      print("LTC Uncompressed: ", add2)
            #    print("LTC Segwit: ", add3)
          #      print("LTC Bech32: ", add4)
        #        print("--------------------")
            #    with open("found.txt", "a") as f:
              #      f.write(f"LTC Winner!!!\n")
                #    f.write(f"Mnemonic: {words}\n")
                  #  f.write(f"LTC Compressed: {add1}\n")
                    #f.write(f"LTC Uncompressed: {add2}\n")
             #       f.write(f"LTC Segwit: {add3}\n")
               #     f.write(f"LTC Bech32: {add4}\n")
               # found = True"""//

            if add1 in eth_bloom or add2 in eth_bloom or add3 in eth_bloom or add4 in eth_bloom:
                print("ETH MATCH FOUND!!!")
                print("Words: ", words)
                print("--------------------")
                print("ETH Address: ", add1)
                print("--------------------")
                with open("found.txt", "a") as f:
                    f.write(f"ETH Winner!!!\n")
                    f.write(f"Mnemonic: {words}\n")
                    f.write(f"ETH Address: {add1}\n")
                found = True

  # // """        if add1 in dash_bloom or add2 in dash_bloom or add3 in dash_bloom or add4 in dash_bloom:
  #              print("DASH MATCH FOUND!!!")
   #             print("Words: ", words)
    #            print("--------------------")
      #          print("DASH Address: ", add1)
      #          print("--------------------")
       #         with open("found.txt", "a") as f:
         #           f.write(f"DASH Winner!!!\n")
           #         f.write(f"Mnemonic: {words}\n")
             #       f.write(f"DASH Address: {add1}\n")
               # found = True"""

#    """        if add1 in doge_bloom or add2 in doge_bloom or add3 in doge_bloom or add4 in doge_bloom:
  #              print("DOGE MATCH FOUND!!!")
    #            print("Words: ", words)
      #          print("--------------------")
        #        print("DOGE Address: ", add1)
          #      print("--------------------")
            #    with open("found.txt", "a") as f:
       #             f.write(f"DOGE Winner!!!\n")
         #           f.write(f"Mnemonic: {words}\n")
           #         f.write(f"DOGE Address: {add1}\n")
             #   found = True"""//

            if not found:
                print("Searching...........", words)

#searchjit = jit(nopython=True)(search)
allowed_strengths = [128, 160, 192, 224, 256]

start_bit_range = int(input("Enter the starting bit range (128, 160, 192, 224, or 256): "))
end_bit_range = int(input("Enter the ending bit range (128, 160, 192, 224, or 256): "))
num_cores = int(input("Enter the number of cores to utilize: "))
language_choice = int(input("Enter the language choice:\n1. English\n2. French\n3. Spanish\n4. Italian\n"))

# Map the language choice to the respective mnemonic language
language_mapping = {
    1: "english",
    2: "french",
    3: "spanish",
    4: "italian"
}

language = language_mapping.get(language_choice)

# Filter the allowed strengths based on the user input
allowed_strengths = [strength for strength in allowed_strengths if start_bit_range <= strength <= end_bit_range]

if not allowed_strengths:
    print("Invalid input. Please enter valid bit ranges (128, 160, 192, 224, or 256).")
elif not language:
    print("Invalid language choice.")
else:
    num_cores = min(num_cores, multiprocessing.cpu_count())

    # Maintain a set of processed words to avoid duplicates
    processed_words = set()

    while True:
        # Generate a batch of words
        mnemo = Mnemonic(language)
        words_batch = [mnemo.generate(strength=128) for _ in range(num_cores)]

        threads = []

        for words in words_batch:
            if words not in processed_words:
                processed_words.add(words)
                t = threading.Thread(target=search, args=(words, mnemo, allowed_strengths))
                t.start()
                threads.append(t)

        for t in threads:
            t.join()
