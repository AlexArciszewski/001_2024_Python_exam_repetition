# import nazwa pakietu nazwa modułu

import pakiet_954.trabka
import pakiet_954.perkusja

# Wywołanie nazwa pakietu nazwa modułu nazwa funkji
pakiet_954.trabka.graj()
pakiet_954.perkusja.graj2()


print("B")
# import modulu z pakietu


from pakiet_954 import trabka
from pakiet_954 import perkusja
trabka.graj()
perkusja.graj2()


print("C")
#import pozwalający uzycie nazwy funkcji w kodzie


from pakiet_954.trabka import graj
from pakiet_954.perkusja import graj2

graj()
graj2()
# gdyby funkcje nazywaly sie taks amo byłby problem i dolna nadpisze górną


print("D")
#import pozwalający uzycie nazwy funkcji w kodzie z aliasami

from pakiet_954.trabka import graj as halas_01
from pakiet_954.perkusja import graj2 as halas_02

halas_01()
halas_02()
