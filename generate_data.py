import csv, random, os
from datetime import datetime, timedelta

random.seed(42)
OUT = 'output'

# === FINCAS AND LOTS ===
fincas = [
    ('La Esperanza', 'Planeta Rica', 'Limon Tahiti', ['L1','L2','L3','L4','L5']),
    ('El Porvenir', 'Planeta Rica', 'Limon Tahiti', ['L1','L2','L3']),
    ('San Jose', 'Puente Iglesias', 'Limon Tahiti', ['L1','L2','L3','L4']),
    ('La Pradera', 'Puente Iglesias', 'Naranja Valencia', ['N1','N2','N3','N4','N5']),
    ('El Vergel', 'Puente Iglesias', 'Naranja Valencia', ['N1','N2','N3']),
    ('Los Naranjos', 'Puente Iglesias', 'Naranja Valencia', ['N1','N2']),
]

# === 1. OPERACIONES-FINCAS.CSV (~200 rows) ===
rows = []
start = datetime(2025, 10, 6)
for week in range(16):
    fecha = start + timedelta(weeks=week)
    semana_str = f'S{week+1}'
    fecha_str = fecha.strftime('%Y-%m-%d')
    for finca, municipio, fruta, lotes in fincas:
        selected = random.sample(lotes, min(random.randint(2,3), len(lotes)))
        for lote in selected:
            ha = random.uniform(3, 12)
            if finca == 'La Esperanza' and lote == 'L3':
                rend = random.uniform(1.2, 2.0)
            elif finca == 'El Vergel' and 9 <= week <= 11:
                rend = random.uniform(5.5, 7.0)
            else:
                rend = random.uniform(2.5, 4.8) if 'Limon' in fruta else random.uniform(3.0, 5.5)

            ton = round(ha * rend, 1)
            lluvia = round(random.uniform(5, 80) if week < 8 else random.uniform(40, 160), 1)
            if 12 <= week <= 13:
                lluvia = round(random.uniform(0, 8), 1)

            cal_exp = round(random.uniform(55, 82), 1)
            if finca == 'San Jose':
                cal_exp = round(random.uniform(35, 55), 1)
            cal_nac = round(random.uniform(10, 30), 1)
            descarte = round(100 - cal_exp - cal_nac, 1)

            jornales = random.randint(4, 18)
            costo_jornal = random.choice([52000, 55000, 58000, 60000])

            incidencias = random.choices(
                ['Ninguna','Acaros','Gomosis','Antracnosis','Trips','Fumagina','Ninguna','Ninguna'],
                k=1
            )[0]

            rows.append([semana_str, fecha_str, finca, municipio, fruta, lote,
                        round(ha,1), ton, round(rend,2), lluvia, cal_exp, cal_nac, descarte,
                        jornales, costo_jornal, incidencias])

random.shuffle(rows)
rows = sorted(rows[:210], key=lambda r: (r[0], r[2]))

with open(os.path.join(OUT, 'operaciones-fincas.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Semana','Fecha','Finca','Municipio','Fruta','Lote','Hectareas','Toneladas_Cosechadas',
                'Rendimiento_Ton_Ha','Lluvia_mm','Calidad_Export_%','Calidad_Nacional_%','Descarte_%',
                'Jornales','Costo_Jornal_COP','Incidencia_Fitosanitaria'])
    w.writerows(rows)

print(f'operaciones-fincas.csv: {len(rows)} rows')

# === 2. RECLAMOS-CALIDAD.CSV (~80 rows) ===
clientes = ['FreshDirect USA','Citrus World NL','TropiFruit UK','Frutas del Pacifico','Exito','Jumbo',
            'PriceSmart','Carulla','Makro','La 14','Super Inter','Olimpica','Mediterranean Foods ES',
            'FruitOne DE','Global Citrus Trading']
paises = {'FreshDirect USA':'USA','Citrus World NL':'Paises Bajos','TropiFruit UK':'Reino Unido',
          'Mediterranean Foods ES':'Espana','FruitOne DE':'Alemania','Global Citrus Trading':'Emiratos Arabes',
          'Frutas del Pacifico':'Colombia','Exito':'Colombia','Jumbo':'Colombia','PriceSmart':'Colombia',
          'Carulla':'Colombia','Makro':'Colombia','La 14':'Colombia','Super Inter':'Colombia','Olimpica':'Colombia'}
calibres_limon = ['36','40','42','48','54']
calibres_naranja = ['56','64','72','88','100']
tipos_reclamo = ['Fruta con manchas','Calibre inconsistente','Madurez prematura','Dano mecanico',
                 'Presencia de plagas','Pudricion','Temperatura contenedor','Peso incorrecto',
                 'Etiquetado erroneo','Residuos de agroquimicos']

reclamos = []
for i in range(70):
    fecha = start + timedelta(days=random.randint(0, 112))
    cliente = random.choice(clientes)
    pais = paises[cliente]
    fruta = random.choice(['Limon Tahiti','Naranja Valencia'])
    calibre = random.choice(calibres_limon if 'Limon' in fruta else calibres_naranja)
    contenedor = f'CONT-{random.randint(1000,9999)}'
    tipo = random.choice(tipos_reclamo)
    if pais != 'Colombia':
        severidad = random.choices(['Alta','Media','Baja'], weights=[40,40,20], k=1)[0]
    else:
        severidad = random.choices(['Alta','Media','Baja'], weights=[15,35,50], k=1)[0]

    cantidad = round(random.uniform(50, 2500), 0)
    valor = round(cantidad * random.uniform(0.3, 1.2), 2) if pais != 'Colombia' else round(cantidad * random.uniform(800, 2500) / 1000, 2)
    moneda = 'USD' if pais != 'Colombia' else 'COP'
    estado = random.choices(['Resuelto','En proceso','Pendiente'], weights=[50,30,20], k=1)[0]
    dias = random.randint(1, 30) if estado == 'Resuelto' else (random.randint(1,15) if estado == 'En proceso' else 0)

    causas = ['Error en seleccion','Cadena de frio rota','Manejo postcosecha','Plaga en campo',
              'Error de empaque','Transporte inadecuado','Almacenamiento prolongado']
    causa = random.choice(causas)

    reclamos.append([f'REC-2025{i+1:03d}', fecha.strftime('%Y-%m-%d'), cliente, pais, fruta,
                     calibre, contenedor, tipo, severidad, int(cantidad),
                     f'{valor}', moneda, estado, dias, causa])

# Inject anomaly: TropiFruit UK gets extra complaints
for i in range(12):
    fecha = start + timedelta(days=random.randint(0, 112))
    reclamos.append([f'REC-2025{70+i+1:03d}', fecha.strftime('%Y-%m-%d'), 'TropiFruit UK', 'Reino Unido',
                     'Limon Tahiti', random.choice(calibres_limon), f'CONT-{random.randint(1000,9999)}',
                     random.choice(['Calibre inconsistente','Fruta con manchas','Madurez prematura']),
                     'Alta', random.randint(200,1500), round(random.uniform(100,800),2), 'USD',
                     random.choice(['Resuelto','En proceso','Pendiente']),
                     random.randint(1,25), random.choice(['Error en seleccion','Manejo postcosecha'])])

reclamos.sort(key=lambda r: r[1])
reclamos = reclamos[:82]

with open(os.path.join(OUT, 'reclamos-calidad.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['ID_Reclamo','Fecha','Cliente','Pais_Destino','Fruta','Calibre','Contenedor',
                'Tipo_Reclamo','Severidad','Cantidad_Kg','Valor_Reclamado','Moneda','Estado',
                'Dias_Resolucion','Causa_Raiz'])
    w.writerows(reclamos)

print(f'reclamos-calidad.csv: {len(reclamos)} rows')

# === 3. PIPELINE-EXPORTACION.CSV (~30 rows) ===
prospectos_data = [
    ('Frudelca','Colombia','Limon Tahiti',150,'Alianza estrategica'),
    ('LimeFresh Inc','USA','Limon Tahiti',200,'Contacto inicial'),
    ('Citrus Europe BV','Paises Bajos','Limon Tahiti',180,'Propuesta enviada'),
    ('Al Rajhi Foods','Arabia Saudita','Limon Tahiti',120,'Negociacion'),
    ('Fresh4U Ltd','Reino Unido','Naranja Valencia',100,'Contacto inicial'),
    ('Rewe Group','Alemania','Naranja Valencia',250,'Propuesta enviada'),
    ('Carrefour LATAM','Brasil','Limon Tahiti',300,'Negociacion'),
    ('MercaFresh','Chile','Naranja Valencia',80,'Contacto inicial'),
    ('Loblaws','Canada','Limon Tahiti',150,'Due diligence'),
    ('Gulf Citrus Trading','Emiratos Arabes','Limon Tahiti',200,'Propuesta enviada'),
    ('Conaprole Frutas','Uruguay','Naranja Valencia',60,'Contacto inicial'),
    ('JBS Frutas','Brasil','Limon Tahiti',180,'Negociacion'),
    ('Whole Foods','USA','Limon Tahiti',250,'Due diligence'),
    ('Albert Heijn','Paises Bajos','Naranja Valencia',120,'Propuesta enviada'),
    ('Migros','Suiza','Limon Tahiti',90,'Contacto inicial'),
    ('Cencosud','Colombia','Naranja Valencia',200,'Contrato firmado'),
    ('D1','Colombia','Limon Tahiti',350,'Contrato firmado'),
    ('Ara','Colombia','Limon Tahiti',180,'Negociacion'),
    ('Tottus','Peru','Limon Tahiti',100,'Propuesta enviada'),
    ('SuperMaxi','Ecuador','Naranja Valencia',70,'Contacto inicial'),
    ('Freshmark SA','Sudafrica','Limon Tahiti',150,'Contacto inicial'),
    ('Zespri Citrus','Nueva Zelanda','Limon Tahiti',80,'Contacto inicial'),
    ('Metro AG','Alemania','Limon Tahiti',200,'Propuesta enviada'),
    ('Grupo Exito Export','Colombia','Naranja Valencia',300,'Negociacion'),
    ('PriceSmart Export','Panama','Limon Tahiti',120,'Due diligence'),
    ('Walmart Mexico','Mexico','Limon Tahiti',400,'Contacto inicial'),
    ('Frutas Montecito','Costa Rica','Naranja Valencia',60,'Contacto inicial'),
    ('La Colonia','Honduras','Limon Tahiti',50,'Propuesta enviada'),
    ('Distribuidora Tropico','Rep. Dominicana','Limon Tahiti',90,'Negociacion'),
    ('Aldi Sud','Alemania','Limon Tahiti',300,'Contacto inicial'),
]

etapas_prob = {'Contacto inicial':15,'Propuesta enviada':35,'Negociacion':55,'Due diligence':70,'Contrato firmado':95,'Alianza estrategica':50}
certs = ['GlobalGAP','USDA Organic','ICA Export','Rainforest Alliance','Ninguna especial','HACCP','BRC']
nombres = ['Maria','Carlos','Juan','Andrea','Diego','Laura']
apellidos = ['Garcia','Lopez','Martinez','Rodriguez','Hernandez','Torres']
proximos = ['Enviar muestras','Llamada de seguimiento','Visita a planta','Enviar cotizacion',
            'Negociar terminos','Firmar contrato','Revisar certificaciones']

pipeline = []
for p, pais, fruta, vol, etapa in prospectos_data:
    contacto = f'{random.choice(nombres)} {random.choice(apellidos)}'
    valor = round(vol * random.uniform(0.8, 1.5) * 12, 0)
    cert = random.choice(certs)
    prox = random.choice(proximos)
    fecha_cierre = (start + timedelta(days=random.randint(30, 180))).strftime('%Y-%m-%d')
    prob = etapas_prob[etapa]
    pipeline.append([p, pais, contacto, fruta, vol, f'{valor:.0f}', etapa, cert, prox, fecha_cierre, prob])

with open(os.path.join(OUT, 'pipeline-exportacion.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Prospecto','Pais','Contacto','Fruta','Volumen_Ton_Mes','Valor_Anual_USD_k',
                'Etapa','Certificacion_Requerida','Proximo_Paso','Fecha_Cierre_Estimada','Probabilidad_%'])
    w.writerows(pipeline)

print(f'pipeline-exportacion.csv: {len(pipeline)} rows')

# === 4. NOTAS-OPERATIVAS.TXT ===
notas = """NOTAS OPERATIVAS - SON DEL CAUCA
Director Operativo: Daniel Velez Molina
Periodo: Octubre 6 - Noviembre 2, 2025

======================================================================
SEMANA 1 (Oct 6 - Oct 12)
======================================================================

Produccion total: 487 toneladas (Limon: 312 ton, Naranja: 175 ton)
Rendimiento promedio: 3.4 ton/ha (Limon), 4.1 ton/ha (Naranja)
Lluvia acumulada: 42 mm promedio

Resumen:
Semana estable en general. La Esperanza reporto rendimiento bajo en el Lote L3 por tercera semana consecutiva - el rendimiento cayo a 1.6 ton/ha cuando el promedio de la finca es 3.2. Agronomia sugiere posible agotamiento de suelo o problema de riego en ese lote. Se programo analisis de suelo para la proxima semana.

Exportaciones: Se despacharon 3 contenedores a Citrus World NL (limon calibre 42-48). Calidad de exportacion en 71% promedio. El cliente reporto satisfaccion con la ultima carga.

Incidencias: Se detectaron acaros en La Esperanza L1 y L2. Se aplico protocolo de fumigacion preventiva. Costo adicional estimado: $3.2M COP.

Personal: 127 jornales totales. Costo promedio $55,000/jornal. Rendimiento por jornal estable.

Pendientes:
- Analisis de suelo La Esperanza L3 (urgente)
- Revision de protocolo de riego en Puente Iglesias
- Cotizacion para nueva fumigadora

======================================================================
SEMANA 2 (Oct 13 - Oct 19)
======================================================================

Produccion total: 523 toneladas (Limon: 338 ton, Naranja: 185 ton)
Rendimiento promedio: 3.6 ton/ha (Limon), 4.3 ton/ha (Naranja)
Lluvia acumulada: 58 mm promedio

Resumen:
Aumento de produccion del 7.4% respecto a semana anterior. Los lotes de Puente Iglesias estan en pico de cosecha. San Jose sigue siendo la finca con menor porcentaje de calidad de exportacion - solo 42% esta semana, muy por debajo del target de 65%. El problema parece ser manchas en la cascara por exceso de humedad. Se ajusto calendario de fumigacion.

El analisis de suelo de La Esperanza L3 confirmo deficiencia de zinc y boro. Se programo plan de fertilizacion correctiva con costo de $4.8M COP. Esperamos ver mejora en 6-8 semanas.

Exportaciones: 4 contenedores despachados (2 USA, 1 NL, 1 UK). TropiFruit UK reporto reclamo por calibre inconsistente en contenedor CONT-3847 - es el tercer reclamo en 2 meses. Comercio exterior (Kevin) esta revisando el proceso de seleccion con la planta empacadora.

Compras: Tomas reporta que el proveedor de cajas de carton subio precio 12%. Se estan evaluando 2 alternativas.

Pendientes:
- Plan correctivo San Jose (calidad exportacion)
- Seguimiento reclamo TropiFruit UK
- Evaluar proveedores alternativos de empaque

======================================================================
SEMANA 3 (Oct 20 - Oct 26)
======================================================================

Produccion total: 498 toneladas (Limon: 310 ton, Naranja: 188 ton)
Rendimiento promedio: 3.3 ton/ha (Limon), 4.5 ton/ha (Naranja)
Lluvia acumulada: 95 mm promedio

Resumen:
Lluvias fuertes afectaron la cosecha de limon, especialmente en Planeta Rica. Caminos de acceso a La Esperanza estuvieron intransitables martes y miercoles - se perdieron 2 dias de cosecha. Impacto estimado: 40-50 toneladas no cosechadas.

El Vergel (naranja) empezo a mostrar rendimientos inusualmente altos: 5.8 ton/ha en N1, 6.2 ton/ha en N2. Agronomia cree que es el pico de la curva de produccion del ciclo. Se reforzo cuadrilla para aprovechar.

Reclamos: TropiFruit UK abrio otro reclamo (CONT-4102, fruta con manchas). Total de reclamos acumulados con ese cliente: 4 en el trimestre, todos de alta severidad. Recomiendo reunion urgente con el cliente y revision completa de la cadena de frio hasta UK.

Finanzas: Aida reporta que la facturacion del mes va en $1,200M COP, 8% arriba del presupuesto. El costo de jornales subio por las lluvias (mas horas de transporte).

Junta Directiva: Camila esta preparando el informe trimestral. Necesita consolidar datos de produccion, calidad, exportacion y costos de las 6 fincas. Actualmente lo hace manual en Excel - toma ~3 dias.

Pendientes:
- Reunion TropiFruit UK (urgente - riesgo de perder cliente)
- Refuerzo cosecha El Vergel (ventana de produccion alta)
- Apoyo a Camila con datos para informe trimestral

======================================================================
SEMANA 4 (Oct 27 - Nov 2)
======================================================================

Produccion total: 465 toneladas (Limon: 290 ton, Naranja: 175 ton)
Rendimiento promedio: 3.1 ton/ha (Limon), 4.0 ton/ha (Naranja)
Lluvia acumulada: 4 mm promedio

Resumen:
SEQUIA. Caida abrupta de lluvias - de 95mm la semana pasada a 4mm esta semana. Impacto directo en rendimiento de limon. Si la tendencia continua la proxima semana, necesitamos activar riego suplementario en Planeta Rica. Costo estimado: $8.5M COP/semana.

San Jose mejoro calidad de exportacion a 48% (vs 42% hace 2 semanas) tras ajuste de fumigacion, pero sigue por debajo del target del 65%. El problema puede ser estructural - la ubicacion de la finca recibe mas humedad que las demas.

La Esperanza L3 muestra los primeros signos de recuperacion tras fertilizacion: rendimiento subio de 1.6 a 1.9 ton/ha. Aun lejos del objetivo (3.0+) pero tendencia positiva.

El Vergel: los rendimientos excepcionales de naranja se normalizaron (bajaron a 4.2 ton/ha). Se cosecho el pico correctamente gracias al refuerzo de cuadrilla.

Comercial: Se cerro contrato con Cencosud (naranja, 200 ton/mes, $COP). Pipeline de exportacion tiene 30 prospectos activos, 3 en etapa de due diligence (Loblaws, Whole Foods, PriceSmart Export). Frudelca aparece como alianza estrategica potencial - compartir volumenes para cumplir contratos grandes.

Talento Humano: Sara reporta alta rotacion en jornaleros de Planeta Rica (15% mensual). Se propone bono de permanencia de $200,000 COP/mes para reducir rotacion.

Recomendaciones para la junta:
1. Invertir en riego suplementario para Planeta Rica (ROI estimado en 1 cosecha)
2. Evaluar reclasificacion de San Jose como finca de mercado nacional (no exportacion)
3. Avanzar conversaciones con Frudelca para alianza de volumenes
4. Aprobar bono de permanencia para jornaleros (costo: ~$12M COP/mes, ahorro en rotacion: ~$18M)
5. Automatizar consolidacion de datos para informes de junta - actualmente toma 3 dias manuales
"""

with open(os.path.join(OUT, 'notas-operativas.txt'), 'w', encoding='utf-8') as f:
    f.write(notas)

print('notas-operativas.txt: written')
print('All demo data generated successfully.')
