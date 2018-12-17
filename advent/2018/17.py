from collections import deque, defaultdict

inp = '''
x=469, y=795..816
x=478, y=1441..1442
x=484, y=1286..1289
y=289, x=475..560
x=610, y=1310..1312
x=590, y=1328..1339
y=467, x=502..518
x=494, y=1544..1548
y=1156, x=586..599
x=611, y=1369..1371
y=1737, x=542..549
x=533, y=399..420
y=1719, x=516..531
x=572, y=1685..1697
y=1545, x=592..596
y=1326, x=476..497
x=600, y=645..653
x=495, y=1796..1813
x=533, y=1580..1594
x=572, y=527..536
y=558, x=626..634
y=1594, x=533..566
y=310, x=560..578
x=513, y=139..160
x=481, y=68..72
x=467, y=1302..1308
y=680, x=492..494
y=199, x=553..562
y=1433, x=482..489
x=529, y=1577..1600
x=476, y=68..72
x=634, y=417..441
x=473, y=252..262
y=54, x=547..569
y=902, x=543..561
x=502, y=1731..1742
x=607, y=330..340
y=750, x=465..546
y=1371, x=611..620
x=482, y=1428..1433
x=582, y=1592..1604
y=1334, x=618..636
x=579, y=32..46
y=579, x=577..604
x=535, y=1532..1541
x=559, y=406..419
y=497, x=501..503
y=1797, x=467..489
y=1675, x=574..590
x=518, y=457..467
x=514, y=173..181
y=1739, x=542..549
x=560, y=276..289
x=573, y=1287..1295
x=515, y=1318..1326
y=1170, x=510..518
y=639, x=513..517
y=403, x=524..527
x=588, y=1257..1259
x=614, y=1428..1437
x=487, y=254..265
y=262, x=473..480
y=94, x=556..579
x=581, y=1388..1405
x=561, y=167..182
x=551, y=694..706
x=575, y=145..160
x=497, y=362..367
y=1175, x=510..518
y=827, x=604..624
x=476, y=1626..1640
x=527, y=502..505
x=603, y=385..403
y=574, x=588..591
y=1350, x=552..556
x=524, y=962..964
x=523, y=202..204
y=1355, x=616..633
x=474, y=1480..1500
x=570, y=1428..1438
x=495, y=418..421
x=490, y=1416..1419
x=506, y=1446..1448
y=1138, x=501..508
x=569, y=1106..1116
y=1614, x=555..578
x=616, y=410..429
x=605, y=348..350
x=491, y=1440..1442
y=1096, x=581..592
x=535, y=1808..1810
y=160, x=575..593
x=507, y=1640..1649
x=537, y=494..504
x=546, y=102..109
x=516, y=1142..1155
x=548, y=653..658
x=561, y=435..439
x=556, y=1644..1657
y=788, x=528..530
x=543, y=849..851
y=877, x=499..524
y=1501, x=536..538
x=495, y=1690..1703
x=615, y=1733..1749
y=1369, x=596..599
y=989, x=572..589
x=577, y=475..479
x=521, y=597..599
x=530, y=1490..1504
y=1459, x=498..501
x=615, y=1392..1401
x=599, y=425..439
x=552, y=547..560
x=577, y=1051..1075
x=524, y=698..703
x=530, y=1121..1134
x=543, y=618..640
x=560, y=1771..1799
x=625, y=591..603
x=569, y=348..351
y=270, x=493..504
y=350, x=602..605
x=603, y=1536..1555
x=541, y=1558..1572
x=607, y=842..866
x=592, y=1183..1192
x=566, y=1315..1320
y=1007, x=506..526
y=1041, x=606..625
x=621, y=229..231
x=507, y=918..932
x=572, y=1124..1126
y=242, x=492..499
y=504, x=537..616
y=102, x=613..615
x=613, y=100..102
y=1089, x=595..621
y=211, x=468..496
x=617, y=83..91
x=522, y=1348..1354
x=584, y=722..732
x=561, y=1625..1635
x=487, y=883..891
x=623, y=1050..1063
x=505, y=1594..1614
x=537, y=427..432
x=618, y=1611..1620
y=1777, x=598..615
x=540, y=1532..1541
x=625, y=1738..1744
x=491, y=954..968
y=963, x=602..616
x=520, y=781..792
x=532, y=1421..1437
x=568, y=166..182
x=493, y=883..891
x=503, y=674..683
y=1548, x=494..516
x=514, y=555..559
x=547, y=1646..1660
x=595, y=549..564
y=903, x=513..516
x=555, y=1604..1614
y=186, x=504..520
x=548, y=511..521
y=1475, x=473..476
y=810, x=536..538
y=1796, x=623..625
x=495, y=1186..1198
x=512, y=1640..1649
x=538, y=247..270
y=964, x=465..479
x=494, y=1269..1274
x=518, y=1358..1359
y=987, x=479..491
x=504, y=175..186
x=549, y=150..166
x=537, y=1078..1091
x=569, y=139..163
y=630, x=581..595
y=876, x=552..557
x=620, y=1369..1371
y=964, x=524..565
x=619, y=364..382
y=1600, x=518..529
y=1780, x=479..499
x=583, y=1537..1555
x=524, y=1313..1326
x=614, y=1004..1015
x=522, y=135..145
y=409, x=467..470
y=579, x=530..535
x=574, y=1658..1675
x=593, y=448..457
y=68, x=476..481
y=1242, x=582..602
x=488, y=1609..1611
y=442, x=550..571
x=603, y=1616..1617
x=618, y=1305..1315
x=625, y=1794..1796
y=109, x=546..567
x=543, y=92..102
x=534, y=1785..1799
y=1744, x=622..625
y=1091, x=537..561
y=564, x=595..605
x=616, y=973..1001
x=533, y=1455..1468
x=599, y=1490..1515
x=611, y=1584..1586
x=512, y=671..682
y=852, x=496..509
y=857, x=560..578
y=1274, x=494..499
y=1115, x=479..484
x=596, y=1342..1369
x=547, y=1470..1480
y=1460, x=559..625
y=1308, x=467..470
y=924, x=470..494
x=617, y=777..782
y=855, x=512..552
x=510, y=1170..1175
y=396, x=550..569
x=487, y=1363..1389
x=537, y=1243..1245
x=605, y=548..564
y=307, x=613..615
x=551, y=1220..1221
x=581, y=1203..1205
x=560, y=527..536
x=495, y=542..555
x=556, y=1348..1350
y=1588, x=543..556
x=515, y=530..535
x=541, y=365..378
x=550, y=782..793
x=534, y=1777..1780
y=1102, x=609..619
x=592, y=281..284
x=530, y=779..788
x=602, y=1363..1374
x=541, y=647..663
x=544, y=1036..1039
y=1339, x=571..590
x=503, y=1286..1289
x=609, y=918..941
x=568, y=911..914
x=589, y=1738..1740
y=393, x=561..563
x=560, y=598..604
x=626, y=253..260
x=592, y=810..816
x=523, y=1226..1241
y=949, x=518..542
y=1477, x=563..566
x=577, y=942..946
x=621, y=855..860
x=600, y=1304..1315
x=479, y=1489..1494
y=1105, x=474..478
y=1262, x=574..594
y=351, x=569..573
x=516, y=1543..1548
y=1777, x=485..487
x=565, y=962..964
x=581, y=343..355
x=496, y=1226..1241
y=497, x=594..603
x=631, y=1427..1437
y=1270, x=526..538
x=469, y=1747..1753
x=538, y=807..810
y=1755, x=499..544
y=419, x=559..579
x=533, y=939..945
x=623, y=1340..1352
x=525, y=1370..1395
x=518, y=123..125
x=517, y=38..40
x=589, y=350..358
x=552, y=887..898
x=496, y=588..592
x=526, y=996..1007
x=568, y=475..479
y=374, x=548..555
x=482, y=1805..1816
x=524, y=29..43
y=1753, x=469..472
y=627, x=558..564
x=633, y=1343..1355
x=470, y=175..180
y=340, x=597..607
x=520, y=155..168
y=1113, x=578..580
x=626, y=1340..1352
y=1286, x=519..526
y=38, x=510..517
x=521, y=1319..1326
x=581, y=1408..1420
x=614, y=1651..1658
y=168, x=520..540
x=548, y=362..374
y=378, x=541..561
y=643, x=498..523
x=555, y=1711..1722
x=579, y=81..94
x=484, y=37..58
x=498, y=632..643
y=1799, x=512..514
x=578, y=1603..1614
x=507, y=1113..1116
y=653, x=600..620
x=572, y=1469..1480
x=534, y=54..66
y=816, x=592..608
x=598, y=1651..1658
x=567, y=943..946
x=509, y=461..463
x=479, y=976..987
x=542, y=36..37
y=239, x=492..499
x=594, y=1250..1262
y=1386, x=503..517
y=1178, x=504..526
x=526, y=1778..1780
y=1519, x=509..520
x=619, y=187..203
y=837, x=482..485
x=585, y=1285..1296
x=577, y=1537..1552
x=582, y=1687..1700
x=583, y=1369..1372
y=1055, x=510..536
x=600, y=1004..1015
x=590, y=424..439
y=1494, x=479..483
x=470, y=643..670
x=531, y=1707..1719
x=535, y=1402..1421
x=527, y=114..129
x=568, y=842..854
x=556, y=1586..1588
x=468, y=1727..1735
x=499, y=598..617
y=1677, x=548..565
x=563, y=1098..1110
x=558, y=1054..1065
x=564, y=1056..1068
x=511, y=1455..1468
y=1799, x=534..537
x=467, y=255..265
x=561, y=388..393
x=537, y=95..97
x=479, y=1595..1614
x=617, y=682..685
x=565, y=1714..1719
x=536, y=1036..1055
x=506, y=1357..1359
x=612, y=126..151
y=521, x=527..548
x=583, y=1576..1579
x=566, y=1219..1221
y=291, x=584..607
y=149, x=480..486
x=518, y=531..542
y=465, x=622..634
y=1275, x=567..574
x=503, y=410..430
x=573, y=320..332
y=582, x=524..549
y=670, x=470..480
x=561, y=453..466
x=471, y=1803..1813
x=584, y=275..291
x=520, y=176..186
x=489, y=1787..1797
x=497, y=1690..1703
x=499, y=867..877
x=598, y=1771..1777
x=507, y=548..565
x=607, y=274..291
x=616, y=493..504
x=481, y=758..771
y=1331, x=627..630
x=573, y=348..351
x=607, y=1286..1296
y=260, x=624..626
y=116, x=498..506
y=793, x=550..561
x=499, y=1671..1682
y=1435, x=576..579
x=611, y=1384..1397
y=332, x=550..573
y=1389, x=472..487
y=401, x=590..599
x=618, y=1324..1334
x=556, y=1054..1065
y=666, x=489..510
x=480, y=146..149
x=490, y=62..78
x=585, y=750..775
y=658, x=546..548
x=567, y=1537..1552
y=923, x=520..524
y=747, x=477..479
y=1635, x=519..561
x=487, y=236..245
y=1753, x=499..544
x=612, y=1111..1128
y=495, x=468..475
y=1312, x=608..610
y=1556, x=469..471
y=1438, x=570..593
y=1810, x=535..541
x=530, y=617..640
y=640, x=619..623
x=479, y=939..964
x=593, y=1427..1438
x=478, y=1090..1105
x=579, y=1331..1333
x=560, y=823..835
x=571, y=1387..1405
x=489, y=1427..1433
x=496, y=825..852
y=1015, x=600..614
y=234, x=602..629
x=519, y=1625..1635
y=145, x=522..544
x=515, y=1564..1586
y=1515, x=599..621
x=480, y=252..262
y=499, x=594..603
x=492, y=1609..1611
x=576, y=1685..1697
y=532, x=602..613
x=557, y=113..125
y=228, x=497..548
y=1250, x=479..485
x=621, y=1430..1434
x=615, y=1772..1777
y=1419, x=468..490
y=1555, x=583..603
y=597, x=518..521
y=743, x=596..622
x=602, y=1228..1242
x=619, y=1100..1102
x=564, y=717..730
x=571, y=62..67
y=1660, x=547..563
x=572, y=1226..1237
x=574, y=1273..1275
y=1237, x=562..572
x=487, y=1774..1777
x=583, y=180..200
x=548, y=1296..1301
y=1111, x=578..580
x=590, y=513..532
y=389, x=517..523
x=497, y=756..768
x=482, y=296..301
x=519, y=1281..1286
x=582, y=597..604
x=489, y=1481..1500
x=627, y=265..269
y=895, x=481..499
y=103, x=490..499
y=1433, x=576..579
y=1004, x=518..520
y=1058, x=479..507
y=1039, x=544..547
x=602, y=1786..1798
x=554, y=887..898
y=463, x=509..512
y=356, x=508..515
x=578, y=298..310
x=592, y=1360..1377
x=625, y=1036..1041
x=512, y=842..855
y=66, x=514..534
x=509, y=251..253
x=510, y=113..129
y=1682, x=485..499
x=488, y=756..768
x=518, y=1576..1600
x=605, y=1110..1128
y=1068, x=548..564
y=105, x=602..621
x=572, y=757..778
x=513, y=593..602
x=493, y=1565..1589
x=545, y=475..485
x=548, y=117..121
x=578, y=844..857
x=530, y=1535..1547
y=1586, x=611..621
y=1377, x=574..592
y=816, x=469..478
y=1523, x=552..557
x=518, y=1170..1175
x=483, y=342..351
y=500, x=490..509
x=465, y=1806..1816
x=599, y=373..401
y=617, x=486..499
y=1354, x=519..522
y=1112, x=517..537
y=245, x=487..508
y=1657, x=553..556
x=561, y=1078..1091
x=586, y=1152..1156
x=579, y=670..682
x=595, y=612..630
y=1326, x=524..543
x=629, y=221..234
x=571, y=296..307
x=599, y=265..269
x=539, y=550..563
y=63, x=525..527
x=470, y=923..924
y=1198, x=495..586
x=552, y=1348..1350
y=663, x=541..563
y=1478, x=520..533
x=571, y=447..457
x=543, y=1586..1588
x=596, y=738..743
y=1173, x=539..543
x=479, y=745..747
y=1798, x=589..602
y=439, x=590..599
y=40, x=510..517
x=505, y=589..592
x=567, y=1783..1788
y=1221, x=580..594
x=507, y=1046..1058
x=527, y=319..324
x=470, y=385..409
x=628, y=701..718
y=610, x=546..548
x=570, y=998..1011
y=898, x=552..554
x=607, y=444..453
y=1497, x=583..590
x=597, y=330..340
y=421, x=491..495
x=604, y=889..898
y=1359, x=506..518
x=574, y=911..914
y=1008, x=577..580
x=467, y=385..409
x=604, y=670..686
y=1001, x=616..625
x=626, y=547..558
x=550, y=430..442
x=479, y=1109..1115
x=582, y=1782..1788
x=548, y=1667..1677
y=181, x=511..514
y=1468, x=511..533
y=1799, x=548..560
y=798, x=607..623
x=598, y=445..453
x=513, y=398..420
x=500, y=316..337
y=1738, x=589..591
x=536, y=1488..1501
x=524, y=913..923
y=679, x=519..531
x=566, y=1580..1594
y=151, x=612..628
x=485, y=564..590
x=563, y=388..393
y=851, x=543..546
x=524, y=549..565
x=476, y=1461..1475
x=519, y=1643..1653
x=578, y=214..242
x=514, y=54..66
y=1075, x=577..579
x=508, y=1128..1138
x=526, y=1262..1270
x=541, y=1808..1810
y=479, x=568..577
y=807, x=536..538
y=1126, x=572..594
y=782, x=615..617
x=581, y=1724..1745
y=453, x=598..607
x=504, y=1166..1178
y=1703, x=495..497
y=682, x=512..538
y=1548, x=592..596
y=1614, x=479..505
x=570, y=866..879
x=547, y=1491..1504
y=430, x=482..503
x=469, y=37..58
x=548, y=1771..1799
y=125, x=516..518
x=602, y=526..532
x=522, y=1370..1395
x=483, y=96..118
x=511, y=1421..1437
x=566, y=842..854
x=472, y=362..371
y=1504, x=530..547
x=533, y=196..209
y=1011, x=570..586
x=502, y=1068..1078
x=527, y=512..521
x=555, y=1096..1107
x=610, y=854..860
x=474, y=1091..1105
x=591, y=574..576
x=599, y=1341..1369
y=592, x=496..505
y=204, x=523..527
x=520, y=1002..1004
x=571, y=430..442
x=547, y=1401..1421
x=489, y=1113..1116
x=622, y=1408..1420
x=595, y=1084..1089
y=826, x=575..580
y=1480, x=547..572
x=501, y=1129..1138
y=253, x=509..520
x=527, y=1097..1108
x=559, y=1730..1742
y=1273, x=567..574
x=604, y=824..827
y=718, x=615..628
x=535, y=576..579
y=918, x=559..581
x=607, y=772..798
y=1673, x=555..557
y=576, x=588..591
x=575, y=756..778
x=520, y=1475..1478
x=602, y=423..437
x=563, y=646..663
y=1697, x=524..549
y=457, x=571..593
x=508, y=235..245
x=591, y=1738..1740
y=1047, x=550..570
x=467, y=1788..1797
y=1013, x=465..473
x=633, y=1786..1801
x=587, y=1270..1280
x=517, y=1339..1342
y=189, x=528..532
x=576, y=1018..1029
x=629, y=1712..1718
y=1658, x=598..614
x=534, y=1664..1677
y=265, x=467..487
x=594, y=1125..1126
y=542, x=518..539
x=621, y=298..312
x=623, y=1794..1796
x=625, y=973..1001
x=593, y=1593..1604
x=550, y=913..925
x=590, y=374..401
x=585, y=1369..1372
y=1116, x=489..507
x=563, y=1647..1660
x=525, y=61..63
x=628, y=1362..1374
x=553, y=197..199
x=602, y=297..312
x=493, y=251..270
x=579, y=1052..1075
y=775, x=585..591
x=534, y=592..602
x=614, y=919..941
x=510, y=38..40
x=552, y=871..876
x=590, y=83..91
y=163, x=562..569
x=576, y=1433..1435
x=551, y=117..121
x=558, y=215..242
y=1442, x=478..491
x=470, y=1302..1308
x=613, y=364..382
x=608, y=1310..1312
y=1315, x=600..618
y=324, x=527..529
x=608, y=1576..1579
x=590, y=1657..1675
y=1547, x=530..547
x=506, y=111..116
y=1762, x=487..586
x=536, y=807..810
x=517, y=637..639
y=778, x=572..575
x=543, y=1314..1326
x=481, y=885..895
x=634, y=681..685
x=621, y=1585..1586
y=630, x=551..572
x=527, y=403..416
x=634, y=457..465
y=968, x=491..572
x=564, y=625..627
x=543, y=1165..1173
x=490, y=98..103
y=706, x=477..551
y=91, x=590..617
x=494, y=671..680
y=451, x=499..504
y=716, x=581..605
x=623, y=1430..1434
x=524, y=1686..1697
x=556, y=1288..1295
x=524, y=1067..1078
x=602, y=222..234
x=495, y=315..337
x=494, y=922..924
x=597, y=939..959
x=498, y=111..116
x=561, y=364..378
y=437, x=602..607
x=587, y=1615..1617
x=542, y=936..949
x=550, y=1121..1134
x=581, y=280..290
x=511, y=173..181
x=529, y=95..97
x=527, y=61..63
x=554, y=24..35
x=581, y=1081..1096
y=768, x=488..497
y=1333, x=577..579
x=616, y=386..403
x=482, y=410..430
x=528, y=779..788
y=301, x=482..501
y=1586, x=513..515
x=483, y=1489..1494
x=572, y=955..968
x=521, y=609..618
x=474, y=1155..1176
x=560, y=845..857
x=583, y=973..984
y=166, x=465..481
x=512, y=1799..1802
x=613, y=525..532
y=1722, x=555..577
x=565, y=1668..1677
x=540, y=247..270
x=521, y=1797..1813
x=545, y=801..813
y=358, x=584..589
y=1290, x=614..627
y=1116, x=569..586
x=514, y=918..932
x=514, y=1799..1802
x=487, y=1750..1762
x=566, y=1475..1477
y=1788, x=567..582
x=479, y=1770..1780
x=561, y=781..793
x=629, y=316..335
x=547, y=1534..1547
y=432, x=537..540
y=1326, x=515..521
y=19, x=488..510
y=1078, x=604..619
y=698, x=524..545
x=548, y=1057..1068
x=580, y=1111..1113
y=312, x=602..621
x=512, y=376..392
x=492, y=174..180
x=557, y=1096..1107
y=1801, x=618..633
x=627, y=1321..1331
x=613, y=307..309
x=584, y=349..358
x=488, y=1627..1640
x=477, y=694..706
y=439, x=561..565
x=611, y=670..686
x=497, y=1320..1326
x=571, y=279..290
x=519, y=1348..1354
x=615, y=100..102
y=682, x=565..579
x=580, y=996..1008
y=871, x=552..557
x=623, y=618..640
y=1090, x=494..496
y=78, x=467..490
y=242, x=558..578
y=704, x=589..591
x=535, y=1321..1323
x=619, y=1059..1078
x=636, y=1323..1334
y=1372, x=583..585
x=499, y=98..103
x=589, y=1786..1798
x=468, y=471..495
y=1119, x=627..631
y=182, x=561..568
x=540, y=426..432
x=511, y=611..622
y=1421, x=535..547
x=546, y=587..610
x=498, y=1453..1459
x=562, y=981..990
y=1526, x=547..565
x=485, y=1774..1777
x=548, y=217..228
x=528, y=35..37
y=590, x=485..491
x=521, y=91..102
x=579, y=973..984
y=97, x=529..537
x=600, y=592..603
y=125, x=536..557
x=590, y=841..866
y=1155, x=516..571
x=517, y=1377..1386
x=604, y=569..579
y=1816, x=465..482
x=603, y=497..499
x=501, y=296..301
x=512, y=437..450
x=501, y=1452..1459
x=536, y=782..792
x=526, y=75..86
x=544, y=150..166
x=503, y=490..497
x=479, y=1231..1250
x=552, y=842..855
x=526, y=1166..1178
x=504, y=446..451
y=1108, x=527..531
x=503, y=1376..1386
x=485, y=815..837
y=1552, x=567..577
x=590, y=1495..1497
x=491, y=563..590
y=1617, x=587..603
x=516, y=123..125
x=531, y=1097..1108
x=586, y=999..1011
x=570, y=1176..1181
x=478, y=95..118
x=630, y=1321..1331
x=517, y=1099..1112
y=1019, x=522..526
x=571, y=1142..1155
y=1677, x=506..534
x=577, y=996..1008
x=510, y=10..19
x=596, y=1545..1548
x=517, y=387..389
x=526, y=1013..1019
x=543, y=889..902
y=1529, x=623..631
x=580, y=1209..1221
x=546, y=4..22
y=203, x=599..619
x=579, y=406..419
x=473, y=1460..1475
y=1192, x=592..617
y=307, x=567..571
x=550, y=385..396
x=552, y=1511..1523
x=499, y=1753..1755
x=615, y=702..718
y=1437, x=511..532
x=548, y=588..610
x=557, y=1511..1523
x=536, y=981..990
x=522, y=1014..1019
x=592, y=1081..1096
x=531, y=677..679
y=730, x=540..564
x=621, y=1489..1515
y=231, x=621..623
y=382, x=613..619
x=602, y=347..350
x=605, y=1662..1677
y=1296, x=585..607
x=578, y=1111..1113
y=58, x=469..484
x=545, y=1099..1110
y=698, x=589..591
y=1221, x=551..566
x=623, y=1528..1529
x=482, y=816..837
x=520, y=1499..1519
x=581, y=907..918
x=520, y=912..923
x=486, y=145..149
x=509, y=474..500
x=513, y=637..639
y=663, x=568..578
y=43, x=502..524
x=550, y=319..332
x=565, y=435..439
x=621, y=95..105
x=625, y=1446..1460
x=582, y=1229..1242
y=180, x=470..492
y=35, x=554..572
x=472, y=1364..1389
y=1640, x=476..488
x=550, y=1037..1047
x=509, y=825..852
y=891, x=487..493
y=653, x=546..548
x=492, y=671..680
x=562, y=139..163
x=485, y=1672..1682
x=508, y=329..356
x=544, y=1753..1755
y=1745, x=581..597
x=602, y=96..105
x=496, y=192..211
y=1395, x=522..525
y=1611, x=488..492
x=565, y=670..682
x=527, y=202..204
x=622, y=456..465
x=512, y=461..463
x=617, y=1393..1401
y=946, x=567..577
y=290, x=571..581
x=585, y=467..481
y=941, x=609..614
x=540, y=718..730
x=538, y=1488..1501
y=1295, x=556..573
y=351, x=483..485
y=1735, x=468..484
y=1697, x=572..576
x=539, y=532..542
y=1589, x=465..493
x=565, y=1514..1526
x=484, y=1108..1115
x=538, y=1262..1270
x=499, y=1269..1274
x=592, y=1545..1548
y=160, x=511..513
x=542, y=1737..1739
x=479, y=1047..1058
y=450, x=512..517
x=561, y=757..771
y=1437, x=614..631
y=555, x=489..495
y=683, x=487..503
x=549, y=1686..1697
x=465, y=739..750
y=1128, x=605..612
y=1280, x=559..587
x=480, y=643..670
x=551, y=617..630
x=631, y=1732..1749
x=618, y=1786..1801
x=487, y=1156..1176
y=1780, x=526..534
y=536, x=560..572
y=677, x=519..531
y=1072, x=513..517
x=589, y=976..989
y=209, x=507..533
x=513, y=896..903
x=530, y=1445..1448
y=685, x=617..634
x=518, y=1002..1004
x=560, y=299..310
y=945, x=528..533
x=537, y=1784..1799
x=624, y=252..260
x=532, y=153..162
x=476, y=1319..1326
y=466, x=537..561
x=504, y=251..270
x=592, y=938..959
y=1740, x=589..591
x=622, y=12..33
x=496, y=1078..1090
y=925, x=531..550
y=1074, x=513..517
y=1802, x=512..514
y=866, x=590..607
x=519, y=677..679
x=568, y=649..663
x=490, y=474..500
x=537, y=1321..1323
x=517, y=555..559
x=572, y=616..630
x=491, y=418..421
x=615, y=307..309
y=129, x=510..527
x=567, y=101..109
x=569, y=386..396
x=562, y=197..199
x=555, y=1665..1673
x=546, y=740..750
x=623, y=772..798
x=477, y=1196..1224
x=561, y=344..355
x=473, y=997..1013
x=559, y=1269..1280
y=420, x=513..533
x=576, y=890..898
x=524, y=866..877
y=1321, x=535..537
x=595, y=723..732
x=547, y=1035..1039
x=471, y=1528..1556
x=536, y=758..771
x=517, y=1215..1223
x=516, y=895..903
x=547, y=1513..1526
x=606, y=1611..1620
x=597, y=1723..1745
x=509, y=1500..1519
x=550, y=1244..1245
y=337, x=495..500
x=590, y=542..564
y=505, x=520..527
x=569, y=38..54
y=618, x=516..521
y=932, x=507..514
x=545, y=698..703
x=556, y=81..94
x=513, y=1564..1586
x=507, y=196..209
y=990, x=536..562
y=1257, x=579..588
x=586, y=1187..1198
y=1241, x=496..523
y=33, x=622..627
x=555, y=1558..1572
x=552, y=1316..1320
x=499, y=1769..1780
x=561, y=890..902
x=537, y=1100..1112
y=309, x=613..615
x=529, y=318..324
y=367, x=497..513
y=1369, x=611..620
y=1620, x=606..618
y=1420, x=581..622
x=588, y=574..576
x=552, y=1175..1181
x=581, y=689..716
x=506, y=1663..1677
x=559, y=1019..1029
x=511, y=140..160
y=849, x=543..546
x=515, y=330..356
x=526, y=1281..1286
x=622, y=1738..1744
y=441, x=621..634
x=580, y=808..826
y=559, x=514..517
x=559, y=908..918
x=567, y=1273..1275
x=553, y=1644..1657
x=497, y=217..228
y=1342, x=500..517
x=544, y=134..145
y=1063, x=623..627
x=523, y=632..643
x=529, y=1295..1301
x=631, y=1527..1529
y=355, x=561..581
x=589, y=698..704
x=634, y=546..558
y=1742, x=502..559
x=605, y=690..716
x=619, y=617..640
y=1107, x=555..557
x=612, y=411..429
y=80, x=605..611
y=1245, x=537..550
x=557, y=871..876
x=510, y=531..535
y=1572, x=541..555
x=536, y=1365..1372
y=429, x=612..616
x=574, y=1359..1377
x=486, y=598..617
y=532, x=590..593
x=506, y=996..1007
y=1224, x=477..489
y=914, x=568..574
x=500, y=1340..1342
x=604, y=1060..1078
y=335, x=629..631
x=593, y=513..532
x=622, y=738..743
x=489, y=1196..1224
x=583, y=1494..1497
y=939, x=528..533
y=202, x=523..527
y=166, x=544..549
x=606, y=1037..1041
y=1719, x=565..568
x=602, y=959..963
y=206, x=473..477
y=1718, x=615..629
y=162, x=532..534
y=898, x=576..604
y=403, x=603..616
x=477, y=200..206
y=1430, x=621..623
x=594, y=497..499
x=534, y=153..162
x=531, y=139..141
x=572, y=975..989
y=1813, x=471..473
x=540, y=156..168
x=561, y=1366..1372
x=547, y=38..54
y=771, x=536..561
x=562, y=1225..1237
x=594, y=1209..1221
x=518, y=597..599
x=578, y=648..663
y=535, x=510..515
x=520, y=501..505
y=1151, x=474..479
y=1065, x=556..558
x=563, y=1475..1477
x=539, y=1164..1173
y=22, x=522..546
y=563, x=539..558
x=545, y=1216..1223
x=465, y=997..1013
x=500, y=74..86
y=1700, x=565..582
x=591, y=750..775
y=1677, x=598..605
y=1541, x=535..540
x=530, y=576..579
x=620, y=644..653
x=479, y=1138..1151
x=528, y=939..945
x=491, y=975..987
y=16, x=531..534
x=586, y=1106..1116
x=529, y=377..392
x=570, y=1036..1047
x=518, y=936..949
x=550, y=547..560
x=583, y=33..46
y=284, x=592..594
x=502, y=1642..1653
x=567, y=296..307
x=549, y=1737..1739
y=1323, x=535..537
x=465, y=158..166
x=494, y=1077..1090
y=37, x=528..542
y=1604, x=582..593
x=510, y=1036..1055
x=575, y=808..826
y=560, x=550..552
x=549, y=571..582
y=1029, x=559..576
x=546, y=849..851
x=468, y=1416..1419
x=523, y=387..389
y=1500, x=474..489
y=270, x=538..540
y=1749, x=615..631
x=608, y=811..816
x=604, y=468..481
x=579, y=1433..1435
y=603, x=600..625
x=577, y=569..579
x=559, y=1447..1460
y=1110, x=545..563
y=602, x=513..534
y=371, x=472..476
y=392, x=512..529
x=517, y=437..450
x=488, y=9..19
y=46, x=579..583
x=621, y=1083..1089
x=477, y=745..747
y=565, x=507..524
y=854, x=566..568
x=555, y=362..374
x=478, y=795..816
x=616, y=1342..1355
x=594, y=1384..1397
x=516, y=609..618
x=473, y=1803..1813
y=771, x=473..481
x=520, y=251..253
y=1078, x=502..524
x=627, y=1284..1290
x=467, y=63..78
x=631, y=317..335
y=1813, x=495..521
x=545, y=866..879
x=621, y=418..441
x=465, y=1565..1589
y=813, x=526..545
x=481, y=158..166
y=1181, x=552..570
y=490, x=501..503
y=118, x=478..483
x=501, y=490..497
x=538, y=672..682
y=102, x=521..543
x=532, y=185..189
x=617, y=1184..1192
x=577, y=1712..1722
y=792, x=520..536
y=200, x=571..583
x=499, y=445..451
x=489, y=654..666
y=599, x=518..521
x=615, y=1711..1718
x=469, y=1528..1556
y=604, x=560..582
y=1405, x=571..581
x=557, y=1665..1673
y=1205, x=553..581
x=546, y=653..658
x=586, y=1749..1762
x=476, y=361..371
x=492, y=239..242
x=582, y=542..564
x=571, y=1329..1339
x=574, y=1250..1262
x=502, y=456..467
x=474, y=1138..1151
x=553, y=1203..1205
y=485, x=523..545
x=616, y=959..963
x=614, y=1283..1290
x=546, y=61..67
x=527, y=139..141
y=67, x=546..571
y=879, x=545..570
x=609, y=1101..1102
y=860, x=610..621
y=564, x=582..590
y=1134, x=530..550
x=539, y=823..835
x=627, y=1104..1119
x=623, y=229..231
x=489, y=542..555
y=1223, x=517..545
y=1579, x=583..608
y=1434, x=621..623
y=959, x=592..597
y=1320, x=552..566
x=526, y=801..813
x=487, y=673..683
y=1176, x=474..487
x=531, y=7..16
x=475, y=275..289
y=640, x=530..543
x=599, y=187..203
y=1372, x=536..561
x=577, y=1331..1333
x=510, y=653..666
y=1374, x=602..628
x=581, y=613..630
x=523, y=474..485
x=527, y=612..622
y=1301, x=529..548
x=593, y=145..160
x=499, y=239..242
y=86, x=500..526
x=502, y=29..43
x=465, y=939..964
x=572, y=24..35
y=100, x=613..615
x=627, y=1051..1063
y=481, x=585..604
x=524, y=572..582
x=472, y=1748..1753
x=528, y=185..189
x=517, y=1072..1074
y=1649, x=507..512
x=475, y=472..495
y=141, x=527..531
x=485, y=341..351
x=594, y=281..284
y=269, x=599..627
x=631, y=1105..1119
y=686, x=604..611
x=611, y=59..80
x=627, y=11..33
y=1653, x=502..519
x=605, y=58..80
x=513, y=363..367
x=484, y=1728..1735
y=1352, x=623..626
y=703, x=524..545
x=599, y=1152..1156
x=598, y=1663..1677
x=565, y=1688..1700
x=485, y=1231..1250
y=72, x=476..481
y=1448, x=506..530
x=558, y=549..563
y=1289, x=484..503
y=1259, x=579..588
y=835, x=539..560
y=121, x=548..551
y=1397, x=594..611
x=579, y=1257..1259
x=522, y=3..22
y=416, x=524..527
x=534, y=7..16
x=591, y=698..704
y=622, x=511..527
y=732, x=584..595
x=533, y=1476..1478
x=499, y=886..895
x=536, y=114..125
x=524, y=403..416
x=607, y=423..437
x=571, y=179..200
x=615, y=777..782
x=473, y=757..771
y=1401, x=615..617
x=516, y=1707..1719
x=628, y=127..151
y=984, x=579..583
x=513, y=1072..1074
x=473, y=200..206
x=468, y=192..211
x=537, y=454..466
x=558, y=625..627
x=624, y=823..827
x=568, y=1714..1719
x=531, y=913..925
'''

#inp = '''
#x=495, y=2..7
#y=7, x=495..501
#x=501, y=3..7
#x=498, y=2..4
#x=506, y=1..2
#x=498, y=10..13
#x=504, y=10..13
#y=13, x=498..504
#'''


rows = inp.strip().split('\n')
clay = []
x_idx = defaultdict(list)
y_idx = defaultdict(list)

for row in rows:
    parts = row.split(', ')
    fvar, fnum = parts[0].split('=')[0], int(parts[0].split('=')[1])
    svar, srange = parts[1].split('=')[0], parts[1].split('=')[1]
    slow, shi = [int(n) for n in srange.split('..')]
    #print fvar, fnum, svar, slow, shi
    if fvar == 'x':
        clay.append((fnum, (slow, shi)))
        x_idx[fnum].append((slow, shi))
    else:
        clay.append(((slow, shi), fnum))
        y_idx[fnum].append((slow, shi))

# how much work do we need to do
# well, filter out coords when we do the counting at the end
y_min = float('inf')
y_max = 0
for f, s in clay:
    if type(s) is tuple:
        if s[0] < y_min:
            y_min = s[0]
        if s[1] > y_max:
            y_max = s[1]
    else:
        if s < y_min:
            y_min = s
        if s > y_max:
            y_max = s

x_min = float('inf')
x_max = 0
for f, s in clay:
    if type(f) is tuple:
        if f[0] < x_min:
            miny = f[0]
        if f[1] > x_max:
            maxy = f[1]
    else:
        if f < x_min:
            x_min = f
        if f > x_max:
            x_max = f

#print clay
#print 'X INDEX', x_idx
#print 'y INDEX', y_idx
#print miny, maxy

def has_clay(x, y):
    #print 'has clay', x, y
    if x not in x_idx and y not in y_idx:
        return False
    if x in x_idx:
        #print 'found in xidx', x
        for ylow, yhi in x_idx[x]:
            #print ylow, yhi
            if y >= ylow and y <= yhi: return True
        #print 'no clay frmo x_idx for', x, y
        if y not in y_idx: return False
    assert y in y_idx
    #print 'found in yidx', y
    for xlow, xhi in y_idx[y]:
        if x >= xlow and x <= xhi:
            return True
    return False

#assert has_clay(498, 7)

# water's going to flow sideways in our representation
spring_loc = (500, 0)

water = set()

#q = deque()
q = []
q.append(('spill', 500, 0))

# water is either falling or bubbling up
# sometimes water spills off both sides of a container

def spill(x, y):
    while not has_clay(x, y) and y <= y_max:
        #print x, y
        # part 2- don't add water
        #water.add((x, y))
        y += 1
    if has_clay(x, y):
        q.append(('expand', x, y-1))
        return
    # otherwise we fell out of bounds
    assert y > maxy

# this is when it hits the bottom of a container
# it expands left and right from the center of the stream (x)
# until one of the sides has no clay
# the first row, the bottom needs to have clay
def expand(x, y):
    #print 'expanding from', x, y
    # look right
    # it might be a ledge with no lip
    has_right_wall = True
    has_left_wall = True
    #curr_water = set()

    while has_right_wall and has_left_wall:
        #print 'expanding y', y
        has_right_wall = False
        has_left_wall = False
        # check right
        xi = x
        # TODO: reevaluate this condition
        while (has_clay(xi, y+1) or (xi, y+1) in water) and not has_clay(xi, y):
        #while has_clay(xi, y+1) or not has_clay(xi, y):
            water.add((xi, y))
            xi += 1
        # did we quit because we hit an edge?
        if has_clay(xi, y):
            #print 'expanded right', y, 'found wall at', xi
            has_right_wall = True
        else:
            # if we fell off, start a spill
            #print 'expanded right', y, 'spilling', xi
            q.append(('spill', xi, y))
            # part 2 - remove most recent row
            xi -= 1
            while (xi, y) in water:
                water.remove((xi, y))
                xi -= 1
        # check left
        xi = x
        while (has_clay(xi, y+1) or (xi, y+1) in water) and not has_clay(xi, y):
        #while has_clay(xi, y+1) or not has_clay(xi, y):
            water.add((xi, y))
            #print 'going left', xi, y
            xi -= 1
            #print 'next vars', xi, y+1, has_clay(xi, y+1), (xi, y+1) in water ,not has_clay(xi, y)
        # did we quit because we hit an edge?
        if has_clay(xi, y):
            #print 'expanded left', y, 'found wall at', xi
            has_left_wall = True
        else:
            #print 'expanded left', y, 'spilling', xi
            q.append(('spill', xi, y))
            # part 2 - remove most recent row
            xi += 1
            while (xi, y) in water:
                water.remove((xi, y))
                xi += 1
        # finally, raise the water level
        y -= 1

    # add water from the current expansion
    #water.update(curr_water)

def write_state(i=1):
    with open('state_{}.txt'.format(i), 'w') as f:
        for x in xrange(x_min-1, x_max+1):
            if x == 500:
                f.write('W')
            else:
                f.write(' ')
        f.write('\r\n')
        for y in xrange(y_min, y_max+1):
            for x in xrange(x_min-1, x_max+1):
                if has_clay(x, y):
                    f.write('#')
                elif (x, y) in water:
                    f.write('~')
                else:
                    f.write('.')
            f.write('\r\n')

visited = set()
while q:
    #raw_input()
    #cmd, x, y = q.popleft()
    cmd, x, y = q.pop(0)
    if (cmd, x, y) in visited:
        #print 'ALREADY VISITED', cmd, x, y
        continue
    if cmd == 'spill' and (
            ((cmd, x-1, y) in visited and (x+1, y) not in water) or
            ((cmd, x+1, y) in visited and (x-1, y) not in water)):
        continue
    visited.add((cmd, x, y))
    #print cmd, x, y
    #print q
    #print water
    if cmd == 'spill':
        spill(x, y)
    else:
        assert cmd == 'expand'
        expand(x, y)
    #cleanup_q()

# a hack to fill in water-empty-water gaps
water_mx = float('inf')
water_max = 0
for x, y in list(water):
    if (x, y) in water and (x+1, y) in water and (x+2, y) not in water and (x+3, y) in water and (x+4, y) in water:
        water.add((x+2, y))
    if x < water_mx:
        water_mx = x
    if x > water_max:
        water_max = x

print water_mx, water_max


write_state(0)

#print water
print x_min, x_max
print y_min, y_max
print len([(x, y) for x, y in water if y >= y_min and y <= y_max])
#print [(x, y) for x, y in water if y < y_min or y > y_max]
#print len([(x, y) for x, y in water if y <= y_max])
#print len([(x, y) for x, y in water if y >= y_min])

# 50673 is wrong
# 14807 is wrong
# 17064 is wrong, too low
# 32021 is wrong

# for part 1
# i ran grep '~' -o state_9090909.txt | wc -l -> 31953 which was correct
# so we must be overwriting some clays or something


# for part 2
# 26754 wrong - too high
# problem is that some patterns like #~~~~~..... at the tops of buckets still remain
# cleaned it up by hand in vim
# 26410 was correct
