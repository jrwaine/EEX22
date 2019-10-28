from automaticGuidedVehicle import AGV

try:
    agv = AGV()

    agv.parafusadeira.subir()
    # agv.move(25, 'CIMA')
    # agv.apertar(agv.verificar_parafuso())
    # agv.move(10)
    # agv.move(25, 'MEIO')
    # agv.apertar(90)
    # agv.inicio()
    
    agv.stop()
    
except KeyboardInterrupt:
    agv.stop()