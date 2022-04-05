from transport import Transport 
from bicicle import Bicicle 
from carbon_fiber_bici import Carbon_Fiber_Bici 
from metal_bici import Metal_Bici 



transport_list = [Carbon_Fiber_Bici("abc", "green", 1945), Metal_Bici("pql", "white", 1988) ]


for transport in transport_list:
    transport.run()
    print(transport.color)