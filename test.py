text = """
WMT	Walmart Inc.	169.28	-0.09	-0.05%	3.934M	8.006M	455.741B	28.17	
PG	The Procter & Gamble Company	157.42	-1.22	-0.77%	4.919M	7.509M	370.412B	26.41	
COST	Costco Wholesale Corporation	723.40	-0.76	-0.10%	1.425M	2.203M	320.993B	49.21	
KO	The Coca-Cola Company	59.56	-0.27	-0.45%	15.205M	14.331M	257.502B	24.11	
PEP	PepsiCo, Inc.	167.67	-6.18	-3.55%	12.726M	5.249M	230.523B	27.94	
PM	Philip Morris International Inc.	89.12	+0.11	+0.12%	4.401M	4.952M	138.355B	17.75	
MDLZ	Mondelez International, Inc.	73.17	-1.59	-2.13%	7.415M	6.377M	98.522B	20.21	
MO	Altria Group, Inc.	40.11	+0.02	+0.05%	6.919M	9.471M	70.732B	8.78	
CL	Colgate-Palmolive Company	83.46	-0.80	-0.95%	4.097M	4.735M	68.719B	30.13	
TGT	Target Corporation	146.53	-0.87	-0.59%	2.789M	4.386M	67.647B	18.64	
MNST	Monster Beverage Corporation	55.66	-0.83	-1.47%	3.835M	5.473M	57.911B	37.86	
EL	The Estée Lauder Companies Inc.	143.34	+2.57	+1.83%	2.577M	3.043M	51.384B	110.26	
STZ	Constellation Brands, Inc.	242.55	-0.50	-0.21%	1.219M	1.153M	44.343B	28.11	
KHC	The Kraft Heinz Company	35.97	-0.50	-1.37%	8.189M	8.133M	44.119B	14.86	
KDP	Keurig Dr Pepper Inc.	31.15	-0.34	-1.08%	5.09M	7.529M	43.558B	22.74	
KMB	Kimberly-Clark Corporation	119.81	-0.46	-0.38%	1.287M	1.928M	40.489B	23.00	
HSY	The Hershey Company	195.45	-6.86	-3.39%	2.751M	1.589M	39.969B	21.57	
SYY	Sysco Corporation	79.55	+0.23	+0.29%	1.757M	3.207M	39.602B	19.45	
KVUE	Kenvue Inc.	19.33	0.00	0.00%	22.497M	19.324M	37.017B	21.48	
GIS	General Mills, Inc.	62.34	-1.72	-2.68%	4.257M	4.284M	35.402B	15.17	
KR	The Kroger Co.	45.41	-0.03	-0.07%	3.194M	4.911M	32.669B	17.67	
DLTR	Dollar Tree, Inc.	139.50	-1.40	-0.99%	2.285M	2.293M	30.393B	26.47	
DG	Dollar General Corporation	135.21	-0.44	-0.32%	1.867M	2.722M	29.678B	15.54	
ADM	Archer-Daniels-Midland Company	53.05	+0.35	+0.66%	5.517M	5.536M	28.296B	7.38	
BF-B	Brown-Forman Corporation	56.57	-0.36	-0.63%	841,817	1.701M	27.18B	34.92	
CHD	Church & Dwight Co., Inc.	98.83	-1.11	-1.11%	1.217M	1.461M	24.35B	32.40	
CLX	The Clorox Company	153.20	-1.02	-0.66%	751,828	1.274M	19.013B	243.17	
TSN	Tyson Foods, Inc.	52.58	-1.39	-2.58%	3.104M	2.807M	18.771B	N/A	
K	Kellanova	53.49	-1.45	-2.64%	3.433M	2.772M	18.321B	22.47	
MKC	McCormick & Company, Incorporated	64.65	-1.17	-1.78%	2.111M	1.788M	17.339B	25.65	
HRL	Hormel Foods Corporation	29.06	-0.41	-1.39%	3.148M	3.173M	15.891B	20.04	
LW	Lamb Weston Holdings, Inc.	100.83	-0.05	-0.05%	904,811	1.559M	14.557B	13.08	
SJM	The J. M. Smucker Company	127.90	-3.19	-2.43%	914,270	1.365M	13.576B	12,790.00	
CELH	Celsius Holdings, Inc.	58.39	-0.32	-0.55%	2.487M	4.721M	13.528B	121.65	
CAG	Conagra Brands, Inc.	27.40	-0.70	-2.49%	5.942M	4.617M	13.097B	13.37	
TAP	Molson Coors Beverage Company	60.23	-0.03	-0.05%	2.134M	1.473M	12.993B	51.48	
BG	Bunge Global SA	88.54	+2.04	+2.36%	2.57M	1.38M	12.864B	6.85	
CPB	Campbell Soup Company	41.99	-1.11	-2.58%	2.894M	2.921M	12.517B	15.91	
ACI	Albertsons Companies, Inc.	21.20	-0.15	-0.70%	2.165M	3.054M	12.212B	9.02	
USFD	US Foods Holding Corp.	46.64	-0.37	-0.79%	950,071	1.658M	11.467B	25.91	
PFGC	Performance Food Group Company	71.71	-0.86	-1.19%	1.299M	916,357	11.157B	26.17	
COTY	Coty Inc.	11.62	-0.26	-2.19%	7.405M	4.193M	10.361B	33.20	
ELF	e.l.f. Beauty, Inc.	174.52	+2.98	+1.74%	1.498M	1.484M	9.687B	77.22	
BJ	BJ's Wholesale Club Holdings, Inc.	67.14	+0.48	+0.72%	783,981	1.387M	8.955B	17.95	
COKE	Coca-Cola Consolidated, Inc.	865.00	-14.14	-1.61%	44,935	46,136	8.108B	18.02	
BRBR	BellRing Brands, Inc.	59.38	+0.52	+0.88%	1.687M	1.308M	7.778B	48.28	
INGR	Ingredion Incorporated	108.16	-1.30	-1.19%	303,166	339,786	7.051B	11.27	
DAR	Darling Ingredients Inc.	41.58	+0.47	+1.14%	1.347M	2.153M	6.633B	9.41	
PPC	Pilgrim's Pride Corporation	27.31	+0.02	+0.07%	534,633	607,895	6.467B	170.69	
POST	Post Holdings, Inc.	104.77	-1.70	-1.60%	723,670	829,095	6.358B	22.53	
SFM	Sprouts Farmers Market, Inc.	51.18	+0.42	+0.83%	1.001M	1.23M	5.198B	21.06	
LANC	Lancaster Colony Corporation	188.75	+0.59	+0.31%	102,211	138,001	5.195B	40.16	
IPAR	Inter Parfums, Inc.	152.19	+1.44	+0.96%	100,956	128,059	4.867B	30.87	
OLLI	Ollie's Bargain Outlet Holdings, Inc.	76.51	+0.89	+1.18%	379,596	937,222	4.712B	30.12	
FLO	Flowers Foods, Inc.	22.19	-1.20	-5.13%	2.945M	1.221M	4.685B	34.67	
FIZZ	National Beverage Corp.	48.01	+0.77	+1.63%	126,862	166,308	4.484B	27.43	
SAM	The Boston Beer Company, Inc.	350.27	-1.54	-0.44%	78,046	102,401	4.27B	51.89	
FRPT	Freshpet, Inc.	87.37	-0.24	-0.27%	361,089	545,801	4.214B	N/A	
LOPE	Grand Canyon Education, Inc.	133.55	+1.49	+1.13%	432,781	223,768	4.008B	21.00	
SMPL	The Simply Good Foods Company	35.17	-0.71	-1.98%	1.189M	637,211	3.51B	26.85	
GHC	Graham Holdings Company	722.42	+15.18	+2.15%	15,154	15,211	3.283B	21.60	
NOMD	Nomad Foods Limited	17.16	-0.19	-1.10%	597,182	591,559	2.889B	13.51	
JJSF	J&J Snack Foods Corp.	148.09	+2.07	+1.42%	98,166	89,273	2.87B	36.12	
NWL	Newell Brands Inc.	6.85	-1.60	-18.93%	17.778M	3.846M	2.837B	N/A	
HELE	Helen of Troy Limited	116.52	+0.34	+0.29%	128,512	237,031	2.767B	17.29	
COUR	Coursera, Inc.	17.87	+0.25	+1.42%	1.584M	1.505M	2.726B	N/A	
CALM	Cal-Maine Foods, Inc.	55.56	+0.06	+0.11%	305,168	724,372	2.721B	6.00	
LRN	Stride, Inc.	62.55	+2.43	+4.04%	774,024	679,349	2.713B	15.76	
SPB	Spectrum Brands Holdings, Inc.	85.86	-0.24	-0.28%	417,211	657,052	2.648B	N/A	
GO	Grocery Outlet Holding Corp.	25.55	+0.42	+1.67%	1.046M	1.11M	2.536B	31.54	
PSMT	PriceSmart, Inc.	78.86	+0.56	+0.72%	154,887	165,309	2.406B	21.37	
STRA	Strategic Education, Inc.	98.45	+1.73	+1.79%	87,683	79,613	2.404B	48.26	
THS	TreeHouse Foods, Inc.	42.86	-0.24	-0.56%	363,530	438,462	2.37B	28.38	
DNUT	Krispy Kreme, Inc.	13.56	+0.04	+0.30%	722,231	793,652	2.286B	N/A	
SOVO	Sovos Brands, Inc.	22.26	0.00	0.00%	598,761	985,944	2.258B	N/A	
UDMY	Udemy, Inc.	14.47	+0.20	+1.40%	527,631	849,249	2.219B	N/A	
HIMS	Hims & Hers Health, Inc.	9.87	+0.02	+0.20%	2.327M	2.678M	2.092B	N/A	
LAUR	Laureate Education, Inc.	12.99	-0.03	-0.23%	926,068	693,142	2.044B	19.98	
CENT	Central Garden & Pet Company	41.43	+2.44	+6.25%	401,300	124,038	2.489B	20.51	
EPC	Edgewell Personal Care Company	39.45	-0.02	-0.05%	502,042	395,040	1.97B	19.15	
ATGE	Adtalem Global Education Inc.	50.42	+1.25	+2.54%	520,121	594,467	1.976B	18.07	
AFYA	Afya Limited	20.90	+0.51	+2.50%	83,764	177,970	1.959B	26.46	
MGPI	MGP Ingredients, Inc.	85.44	-0.13	-0.15%	195,180	173,962	1.881B	19.33	
ANDE	The Andersons, Inc.	52.25	-0.08	-0.15%	148,910	186,518	1.764B	27.50	
WMK	Weis Markets, Inc.	59.69	-1.09	-1.79%	136,271	90,029	1.606B	14.31	
VGR	Vector Group Ltd.	9.95	+0.04	+0.40%	1.364M	871,931	1.552B	8.96	
UTZ	Utz Brands, Inc.	18.43	+0.25	+1.38%	841,317	831,131	1.495B	87.76	
IMKTA	Ingles Markets, Incorporated	78.38	-3.45	-4.22%	132,375	71,863	1.489B	7.06	
CHEF	The Chefs' Warehouse, Inc.	34.09	+0.60	+1.79%	323,577	405,532	1.352B	65.56	
TR	Tootsie Roll Industries, Inc.	33.12	+0.27	+0.82%	93,624	73,585	1.327B	26.50	
UVV	Universal Corporation	51.97	-1.61	-3.00%	260,120	203,303	1.277B	9.77	
HLF	Herbalife Ltd.	12.07	-0.29	-2.35%	1.361M	1.336M	1.196B	6.45	
PRDO	Perdoceo Education Corporation	18.07	+0.35	+1.98%	277,463	447,321	1.187B	8.40	
JBSS	John B. Sanfilippo & Son, Inc.	98.88	-0.38	-0.38%	47,684	50,131	1.147B	17.17	
COCO	The Vita Coco Company, Inc.	20.16	-0.01	-0.05%	489,132	694,965	1.145B	32.00	
FDP	Fresh Del Monte Produce Inc.	23.78	-0.13	-0.54%	275,050	224,234	1.144B	10.12	
KLG	WK Kellogg Co	12.43	-0.02	-0.16%	1.164M	1.099M	1.064B	N/A	
AGRO	Adecoagro S.A.	9.83	+0.05	+0.51%	435,126	722,609	1.048B	7.18	
DOLE	Dole plc	10.91	-0.09	-0.82%	279,783	552,404	1.036B	11.86	
NAPA	The Duckhorn Portfolio, Inc.	8.87	+0.20	+2.31%	668,779	971,085	1.023B	15.84	



"""

# Split the text into lines
lines = text.strip().split('\n')

# Extract the first item (symbol) from each line

symbols = [line.split()[0] for line in lines]

print(symbols)
