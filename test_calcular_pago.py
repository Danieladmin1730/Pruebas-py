from calcular_pago import calcular_pago_laboral

def test_pago_jornada_completa_sin_extras():
    resultado = calcular_pago_laboral(1300000, 0, 0, 0, 0, "completa")
    valor_dia = round(1300000 / 30, 2)
    assert resultado["pago_jornada"] == valor_dia
    assert resultado["total_pago"] == valor_dia

def test_pago_jornada_media_sin_extras():
    resultado = calcular_pago_laboral(1300000, 0, 0, 0, 0, "media")
    valor_medio_dia = round((1300000 / 30) / 2, 2)
    assert resultado["pago_jornada"] == valor_medio_dia
    assert resultado["total_pago"] == valor_medio_dia

def test_pago_con_horas_extras():
    resultado = calcular_pago_laboral(1300000, 2, 1, 1, 1, "completa")
    assert resultado["total_pago"] > resultado["pago_jornada"]

def test_pago_total_con_todas_las_extras():
    resultado = calcular_pago_laboral(1300000, 5, 5, 5, 5, "media")
    assert resultado["pago_extra_diurna"] > 0
    assert resultado["pago_extra_nocturna"] > 0
    assert resultado["pago_extra_festiva_diurna"] > 0
    assert resultado["pago_extra_festiva_nocturna"] > 0
    assert resultado["total_pago"] > resultado["pago_jornada"]

def test_valores_con_salario_diferente():
    resultado = calcular_pago_laboral(2000000, 1, 1, 1, 1, "completa")
    assert resultado["valor_hora"] > 0
    assert resultado["valor_dia"] > 0
    assert resultado["total_pago"] > 0
