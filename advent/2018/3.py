from collections import Counter, defaultdict

inp = '''
#1 @ 912,277: 27x20
#2 @ 129,477: 14x12
#3 @ 915,716: 17x23
#4 @ 809,807: 24x16
#5 @ 769,790: 22x13
#6 @ 409,863: 17x10
#7 @ 615,757: 13x25
#8 @ 462,742: 6x3
#9 @ 317,136: 22x22
#10 @ 943,921: 24x14
#11 @ 919,88: 5x16
#12 @ 38,436: 29x26
#13 @ 46,555: 27x21
#14 @ 460,762: 14x14
#15 @ 423,333: 28x29
#16 @ 670,127: 29x26
#17 @ 760,392: 13x13
#18 @ 368,212: 28x18
#19 @ 196,245: 15x28
#20 @ 77,633: 11x13
#21 @ 401,739: 16x17
#22 @ 925,252: 12x13
#23 @ 804,869: 16x24
#24 @ 200,411: 24x11
#25 @ 62,674: 10x12
#26 @ 15,931: 10x28
#27 @ 900,648: 12x20
#28 @ 967,72: 15x26
#29 @ 258,67: 12x13
#30 @ 173,653: 16x10
#31 @ 691,678: 26x18
#32 @ 289,54: 17x20
#33 @ 610,547: 24x28
#34 @ 972,21: 15x24
#35 @ 88,161: 21x22
#36 @ 145,781: 17x15
#37 @ 407,861: 10x25
#38 @ 153,657: 24x23
#39 @ 633,582: 25x18
#40 @ 149,506: 17x27
#41 @ 267,241: 25x20
#42 @ 266,694: 13x28
#43 @ 433,349: 17x16
#44 @ 107,38: 23x28
#45 @ 790,785: 25x28
#46 @ 453,775: 14x17
#47 @ 624,294: 23x14
#48 @ 585,141: 12x24
#49 @ 175,504: 22x20
#50 @ 658,336: 23x28
#51 @ 31,630: 27x15
#52 @ 160,148: 28x10
#53 @ 144,870: 19x29
#54 @ 392,111: 26x19
#55 @ 666,835: 22x11
#56 @ 745,295: 25x26
#57 @ 36,788: 26x10
#58 @ 5,196: 20x16
#59 @ 904,143: 19x16
#60 @ 467,544: 26x27
#61 @ 517,586: 20x22
#62 @ 118,481: 15x25
#63 @ 440,217: 19x15
#64 @ 635,491: 25x13
#65 @ 847,739: 27x28
#66 @ 299,910: 15x26
#67 @ 87,253: 18x17
#68 @ 333,945: 21x16
#69 @ 195,266: 27x11
#70 @ 576,411: 22x28
#71 @ 870,22: 28x14
#72 @ 195,792: 14x11
#73 @ 48,571: 10x16
#74 @ 454,394: 16x19
#75 @ 320,975: 28x13
#76 @ 622,803: 24x26
#77 @ 956,927: 29x23
#78 @ 715,535: 24x22
#79 @ 790,801: 25x23
#80 @ 618,953: 17x11
#81 @ 931,964: 17x19
#82 @ 599,445: 20x14
#83 @ 540,328: 27x21
#84 @ 443,618: 11x25
#85 @ 856,487: 23x26
#86 @ 104,914: 28x17
#87 @ 656,981: 11x18
#88 @ 711,321: 4x15
#89 @ 636,883: 27x24
#90 @ 58,320: 25x27
#91 @ 722,439: 26x12
#92 @ 914,950: 25x29
#93 @ 816,166: 16x25
#94 @ 850,717: 14x27
#95 @ 661,183: 19x10
#96 @ 537,533: 28x17
#97 @ 618,162: 10x23
#98 @ 862,815: 25x21
#99 @ 181,30: 12x10
#100 @ 539,497: 24x24
#101 @ 390,82: 21x13
#102 @ 281,573: 29x12
#103 @ 49,731: 27x29
#104 @ 707,318: 12x22
#105 @ 739,597: 23x13
#106 @ 10,56: 16x15
#107 @ 101,37: 26x17
#108 @ 782,489: 16x28
#109 @ 284,930: 27x16
#110 @ 748,343: 11x17
#111 @ 786,380: 20x22
#112 @ 368,819: 21x15
#113 @ 164,525: 26x12
#114 @ 26,419: 25x27
#115 @ 98,663: 19x11
#116 @ 919,332: 16x25
#117 @ 948,690: 11x25
#118 @ 378,95: 18x10
#119 @ 371,69: 13x23
#120 @ 620,58: 29x29
#121 @ 973,316: 18x13
#122 @ 266,385: 13x11
#123 @ 281,675: 26x21
#124 @ 583,187: 21x17
#125 @ 383,200: 20x15
#126 @ 437,615: 15x14
#127 @ 433,912: 24x20
#128 @ 823,825: 14x19
#129 @ 355,100: 25x26
#130 @ 168,747: 28x22
#131 @ 540,867: 29x27
#132 @ 364,792: 28x16
#133 @ 713,938: 28x17
#134 @ 524,758: 26x29
#135 @ 837,357: 19x21
#136 @ 213,741: 17x19
#137 @ 468,73: 28x16
#138 @ 271,686: 20x23
#139 @ 216,852: 14x17
#140 @ 966,434: 14x22
#141 @ 726,890: 26x29
#142 @ 217,757: 13x17
#143 @ 75,50: 28x16
#144 @ 157,674: 28x20
#145 @ 256,171: 29x10
#146 @ 946,811: 18x12
#147 @ 956,854: 14x28
#148 @ 964,65: 11x10
#149 @ 533,895: 18x18
#150 @ 88,790: 23x25
#151 @ 307,863: 20x24
#152 @ 317,130: 25x12
#153 @ 18,698: 22x27
#154 @ 421,617: 21x20
#155 @ 574,635: 4x17
#156 @ 91,451: 16x27
#157 @ 636,767: 28x12
#158 @ 62,721: 13x17
#159 @ 227,172: 11x23
#160 @ 947,697: 26x17
#161 @ 520,434: 20x23
#162 @ 966,430: 16x16
#163 @ 434,696: 10x23
#164 @ 695,130: 13x23
#165 @ 344,595: 26x26
#166 @ 628,102: 12x16
#167 @ 203,480: 11x23
#168 @ 157,921: 10x16
#169 @ 579,576: 19x10
#170 @ 746,5: 15x17
#171 @ 592,337: 16x29
#172 @ 246,833: 26x14
#173 @ 140,168: 13x13
#174 @ 398,669: 24x29
#175 @ 351,389: 13x21
#176 @ 649,310: 22x23
#177 @ 625,268: 15x23
#178 @ 250,950: 13x26
#179 @ 224,765: 16x28
#180 @ 748,406: 14x14
#181 @ 651,1: 24x11
#182 @ 162,816: 27x13
#183 @ 872,695: 18x18
#184 @ 935,786: 11x11
#185 @ 956,51: 27x13
#186 @ 200,293: 23x12
#187 @ 897,157: 14x26
#188 @ 15,142: 26x14
#189 @ 678,678: 29x23
#190 @ 736,18: 19x29
#191 @ 124,783: 29x16
#192 @ 874,848: 20x11
#193 @ 948,269: 29x27
#194 @ 608,470: 16x12
#195 @ 498,829: 27x23
#196 @ 267,246: 20x17
#197 @ 684,188: 29x16
#198 @ 54,179: 25x18
#199 @ 58,601: 29x16
#200 @ 889,697: 11x22
#201 @ 277,541: 18x12
#202 @ 599,300: 25x18
#203 @ 894,518: 20x11
#204 @ 618,90: 10x20
#205 @ 917,85: 11x29
#206 @ 507,435: 27x16
#207 @ 593,891: 17x26
#208 @ 694,774: 25x17
#209 @ 787,140: 21x24
#210 @ 184,841: 17x19
#211 @ 558,897: 22x28
#212 @ 350,849: 19x13
#213 @ 848,459: 21x22
#214 @ 509,165: 22x23
#215 @ 180,513: 25x19
#216 @ 812,331: 26x14
#217 @ 8,405: 16x22
#218 @ 68,641: 17x24
#219 @ 198,112: 17x23
#220 @ 936,799: 24x11
#221 @ 595,5: 16x28
#222 @ 345,525: 12x24
#223 @ 841,744: 22x24
#224 @ 907,477: 10x18
#225 @ 889,300: 27x15
#226 @ 909,644: 17x29
#227 @ 671,427: 13x15
#228 @ 117,380: 28x23
#229 @ 808,65: 29x12
#230 @ 184,477: 11x23
#231 @ 694,73: 15x20
#232 @ 625,485: 26x28
#233 @ 0,279: 17x15
#234 @ 67,536: 24x17
#235 @ 83,638: 22x13
#236 @ 98,916: 25x28
#237 @ 782,633: 16x10
#238 @ 19,426: 25x17
#239 @ 451,902: 11x24
#240 @ 835,830: 29x24
#241 @ 74,796: 13x22
#242 @ 537,504: 10x12
#243 @ 724,550: 18x29
#244 @ 443,637: 27x26
#245 @ 688,69: 14x24
#246 @ 139,810: 21x17
#247 @ 87,37: 28x26
#248 @ 510,584: 17x29
#249 @ 399,255: 20x13
#250 @ 557,888: 12x17
#251 @ 157,699: 11x26
#252 @ 959,524: 26x26
#253 @ 724,731: 18x26
#254 @ 406,763: 19x22
#255 @ 247,377: 22x12
#256 @ 636,30: 25x28
#257 @ 699,716: 11x20
#258 @ 559,549: 14x13
#259 @ 851,206: 13x18
#260 @ 298,928: 26x16
#261 @ 176,852: 27x22
#262 @ 706,637: 16x25
#263 @ 848,842: 13x26
#264 @ 220,468: 21x19
#265 @ 601,817: 29x14
#266 @ 124,516: 27x24
#267 @ 69,165: 13x20
#268 @ 490,441: 26x26
#269 @ 464,28: 18x18
#270 @ 953,674: 15x29
#271 @ 108,345: 19x28
#272 @ 369,162: 12x29
#273 @ 808,789: 24x13
#274 @ 107,85: 4x7
#275 @ 304,927: 13x14
#276 @ 951,867: 27x19
#277 @ 117,713: 27x24
#278 @ 395,667: 14x28
#279 @ 35,573: 27x23
#280 @ 265,533: 16x19
#281 @ 153,795: 11x10
#282 @ 381,653: 27x17
#283 @ 675,880: 15x23
#284 @ 515,620: 25x10
#285 @ 373,692: 21x18
#286 @ 234,380: 18x21
#287 @ 848,726: 12x16
#288 @ 145,795: 27x15
#289 @ 122,659: 27x11
#290 @ 88,778: 17x27
#291 @ 833,359: 13x26
#292 @ 571,632: 12x25
#293 @ 335,79: 12x17
#294 @ 739,673: 24x10
#295 @ 774,220: 17x16
#296 @ 623,23: 10x15
#297 @ 622,641: 11x24
#298 @ 873,29: 16x25
#299 @ 584,565: 21x13
#300 @ 481,136: 14x22
#301 @ 537,13: 19x20
#302 @ 917,69: 25x20
#303 @ 274,171: 26x27
#304 @ 50,575: 15x24
#305 @ 287,139: 17x14
#306 @ 295,857: 18x12
#307 @ 226,94: 28x17
#308 @ 706,863: 21x18
#309 @ 753,701: 23x10
#310 @ 419,91: 17x29
#311 @ 283,44: 19x25
#312 @ 13,766: 29x23
#313 @ 495,655: 14x22
#314 @ 947,942: 28x13
#315 @ 629,926: 14x28
#316 @ 846,212: 19x27
#317 @ 746,390: 19x23
#318 @ 804,159: 25x20
#319 @ 896,631: 26x23
#320 @ 332,953: 20x25
#321 @ 314,393: 21x28
#322 @ 893,76: 26x20
#323 @ 814,669: 29x25
#324 @ 335,434: 29x28
#325 @ 774,462: 19x17
#326 @ 279,914: 17x18
#327 @ 747,573: 28x18
#328 @ 601,190: 10x11
#329 @ 392,532: 12x26
#330 @ 820,198: 17x28
#331 @ 83,280: 26x12
#332 @ 109,926: 11x25
#333 @ 73,885: 21x29
#334 @ 173,228: 12x28
#335 @ 299,858: 21x18
#336 @ 514,156: 13x23
#337 @ 428,634: 24x20
#338 @ 963,32: 15x24
#339 @ 236,856: 14x23
#340 @ 99,878: 26x12
#341 @ 82,282: 15x15
#342 @ 101,374: 22x15
#343 @ 702,103: 22x25
#344 @ 187,831: 26x13
#345 @ 885,528: 12x15
#346 @ 424,755: 16x20
#347 @ 218,682: 11x13
#348 @ 581,980: 24x12
#349 @ 92,440: 12x18
#350 @ 470,699: 22x21
#351 @ 184,24: 13x12
#352 @ 669,179: 11x25
#353 @ 139,846: 19x15
#354 @ 786,617: 14x26
#355 @ 160,683: 23x24
#356 @ 768,222: 16x26
#357 @ 74,425: 13x11
#358 @ 97,665: 28x22
#359 @ 214,770: 10x15
#360 @ 734,686: 11x11
#361 @ 384,233: 12x26
#362 @ 279,55: 20x26
#363 @ 420,942: 23x13
#364 @ 296,858: 14x10
#365 @ 1,321: 18x25
#366 @ 619,753: 17x17
#367 @ 318,62: 21x16
#368 @ 119,483: 29x20
#369 @ 346,948: 14x24
#370 @ 292,293: 22x17
#371 @ 540,91: 12x23
#372 @ 278,867: 23x21
#373 @ 777,874: 24x11
#374 @ 745,1: 27x17
#375 @ 718,239: 28x21
#376 @ 253,56: 21x28
#377 @ 572,578: 12x28
#378 @ 49,923: 12x28
#379 @ 577,1: 22x20
#380 @ 643,602: 29x15
#381 @ 537,647: 24x28
#382 @ 440,360: 24x15
#383 @ 794,539: 21x15
#384 @ 378,546: 4x3
#385 @ 516,380: 10x23
#386 @ 658,197: 13x22
#387 @ 855,528: 13x24
#388 @ 469,358: 15x25
#389 @ 848,230: 19x15
#390 @ 260,23: 21x21
#391 @ 558,399: 19x28
#392 @ 34,938: 24x22
#393 @ 695,131: 20x14
#394 @ 230,366: 28x22
#395 @ 274,806: 28x15
#396 @ 677,19: 27x29
#397 @ 982,660: 10x29
#398 @ 21,428: 19x8
#399 @ 14,44: 20x25
#400 @ 876,700: 21x14
#401 @ 40,142: 13x22
#402 @ 855,738: 19x25
#403 @ 606,74: 27x25
#404 @ 681,839: 18x21
#405 @ 888,844: 11x18
#406 @ 186,475: 25x15
#407 @ 451,374: 20x17
#408 @ 452,37: 23x19
#409 @ 676,27: 27x18
#410 @ 56,614: 21x16
#411 @ 720,301: 24x28
#412 @ 195,335: 20x25
#413 @ 504,888: 15x14
#414 @ 184,650: 13x27
#415 @ 527,496: 26x27
#416 @ 157,834: 20x24
#417 @ 762,359: 29x22
#418 @ 421,34: 12x13
#419 @ 512,971: 16x13
#420 @ 556,562: 16x7
#421 @ 570,584: 12x17
#422 @ 450,487: 29x18
#423 @ 524,436: 11x18
#424 @ 714,441: 19x29
#425 @ 918,296: 27x24
#426 @ 569,160: 22x13
#427 @ 329,611: 15x12
#428 @ 439,601: 12x19
#429 @ 479,607: 19x16
#430 @ 841,747: 20x16
#431 @ 652,299: 16x25
#432 @ 301,620: 23x13
#433 @ 308,505: 20x18
#434 @ 884,527: 20x21
#435 @ 591,372: 16x25
#436 @ 207,367: 28x19
#437 @ 618,158: 17x20
#438 @ 922,785: 10x28
#439 @ 672,761: 26x28
#440 @ 888,533: 24x23
#441 @ 588,203: 16x15
#442 @ 399,115: 28x18
#443 @ 292,516: 25x26
#444 @ 815,182: 16x17
#445 @ 446,714: 12x24
#446 @ 347,389: 16x28
#447 @ 725,42: 25x24
#448 @ 983,163: 14x17
#449 @ 400,101: 10x20
#450 @ 362,806: 27x24
#451 @ 87,783: 29x20
#452 @ 625,701: 10x15
#453 @ 379,349: 23x12
#454 @ 657,48: 24x10
#455 @ 656,576: 11x18
#456 @ 756,790: 21x11
#457 @ 771,917: 16x15
#458 @ 640,606: 11x29
#459 @ 636,39: 16x26
#460 @ 305,207: 22x16
#461 @ 269,542: 13x16
#462 @ 577,170: 12x21
#463 @ 23,774: 25x15
#464 @ 168,206: 16x26
#465 @ 856,802: 15x19
#466 @ 872,8: 28x11
#467 @ 330,366: 11x19
#468 @ 515,522: 20x16
#469 @ 185,127: 19x12
#470 @ 48,632: 13x15
#471 @ 312,646: 19x21
#472 @ 65,637: 27x20
#473 @ 897,986: 16x10
#474 @ 358,757: 16x10
#475 @ 383,693: 14x19
#476 @ 23,122: 19x13
#477 @ 405,263: 23x15
#478 @ 770,837: 17x27
#479 @ 768,403: 25x12
#480 @ 778,939: 27x20
#481 @ 150,787: 13x19
#482 @ 735,126: 29x19
#483 @ 890,915: 10x29
#484 @ 238,10: 16x23
#485 @ 563,163: 15x13
#486 @ 274,262: 12x27
#487 @ 426,934: 21x22
#488 @ 88,881: 18x15
#489 @ 940,171: 21x20
#490 @ 348,894: 13x19
#491 @ 905,356: 18x13
#492 @ 398,571: 22x26
#493 @ 914,20: 10x28
#494 @ 857,694: 24x28
#495 @ 50,368: 19x26
#496 @ 319,280: 9x7
#497 @ 200,765: 18x26
#498 @ 605,627: 16x21
#499 @ 723,720: 12x11
#500 @ 733,128: 28x25
#501 @ 319,499: 27x18
#502 @ 923,168: 15x25
#503 @ 603,695: 28x24
#504 @ 761,641: 22x14
#505 @ 254,235: 25x11
#506 @ 445,500: 23x11
#507 @ 444,909: 18x15
#508 @ 133,795: 18x10
#509 @ 887,257: 26x27
#510 @ 947,424: 24x16
#511 @ 448,607: 26x26
#512 @ 622,757: 29x12
#513 @ 600,385: 11x14
#514 @ 43,318: 21x21
#515 @ 45,429: 11x22
#516 @ 13,334: 20x19
#517 @ 365,701: 12x21
#518 @ 586,93: 28x26
#519 @ 702,149: 10x13
#520 @ 254,462: 18x26
#521 @ 139,794: 27x28
#522 @ 13,280: 26x23
#523 @ 389,521: 11x19
#524 @ 888,16: 17x28
#525 @ 179,923: 20x29
#526 @ 979,945: 10x12
#527 @ 965,935: 23x13
#528 @ 444,798: 27x21
#529 @ 277,613: 29x10
#530 @ 535,900: 29x22
#531 @ 729,302: 24x23
#532 @ 316,208: 11x23
#533 @ 242,879: 14x27
#534 @ 582,602: 25x10
#535 @ 119,839: 21x20
#536 @ 943,94: 23x18
#537 @ 743,1: 15x24
#538 @ 240,789: 26x21
#539 @ 890,648: 18x27
#540 @ 485,642: 24x20
#541 @ 230,530: 24x25
#542 @ 787,256: 10x22
#543 @ 772,793: 21x17
#544 @ 192,788: 26x25
#545 @ 558,426: 22x14
#546 @ 306,50: 26x22
#547 @ 900,319: 25x14
#548 @ 583,890: 21x11
#549 @ 73,925: 19x12
#550 @ 604,449: 28x28
#551 @ 545,546: 20x20
#552 @ 45,380: 14x22
#553 @ 736,920: 16x19
#554 @ 726,431: 27x16
#555 @ 451,626: 15x23
#556 @ 766,627: 26x26
#557 @ 476,178: 24x26
#558 @ 728,839: 27x11
#559 @ 904,245: 24x24
#560 @ 959,103: 17x23
#561 @ 328,620: 22x15
#562 @ 506,662: 10x29
#563 @ 24,394: 26x18
#564 @ 574,151: 20x13
#565 @ 211,903: 27x26
#566 @ 742,29: 23x26
#567 @ 730,734: 21x13
#568 @ 598,1: 17x12
#569 @ 257,833: 25x17
#570 @ 8,683: 24x29
#571 @ 743,677: 27x19
#572 @ 812,396: 24x21
#573 @ 37,123: 18x23
#574 @ 586,193: 21x10
#575 @ 697,750: 18x14
#576 @ 584,250: 14x19
#577 @ 366,213: 21x13
#578 @ 69,814: 22x10
#579 @ 578,153: 12x7
#580 @ 784,377: 26x26
#581 @ 105,663: 23x15
#582 @ 212,334: 21x17
#583 @ 726,679: 26x18
#584 @ 622,835: 18x13
#585 @ 493,45: 17x19
#586 @ 675,652: 25x22
#587 @ 896,235: 25x15
#588 @ 734,666: 23x12
#589 @ 371,785: 27x17
#590 @ 495,410: 14x23
#591 @ 951,343: 26x13
#592 @ 849,510: 19x12
#593 @ 812,790: 24x21
#594 @ 221,861: 19x20
#595 @ 259,128: 21x17
#596 @ 150,269: 28x12
#597 @ 77,912: 15x18
#598 @ 730,568: 26x26
#599 @ 380,101: 19x14
#600 @ 187,789: 16x13
#601 @ 788,506: 27x17
#602 @ 840,782: 28x22
#603 @ 448,981: 27x10
#604 @ 883,591: 10x28
#605 @ 381,776: 15x13
#606 @ 101,318: 24x18
#607 @ 148,700: 26x22
#608 @ 627,272: 14x28
#609 @ 964,752: 23x26
#610 @ 647,891: 28x29
#611 @ 461,42: 6x7
#612 @ 555,866: 14x19
#613 @ 42,735: 10x25
#614 @ 671,893: 10x17
#615 @ 93,838: 15x13
#616 @ 578,298: 17x23
#617 @ 282,682: 20x25
#618 @ 632,355: 16x26
#619 @ 449,66: 13x29
#620 @ 97,409: 16x17
#621 @ 706,219: 20x29
#622 @ 703,856: 18x24
#623 @ 804,797: 18x10
#624 @ 434,941: 11x13
#625 @ 981,36: 10x15
#626 @ 810,334: 15x24
#627 @ 746,833: 26x12
#628 @ 605,572: 10x16
#629 @ 855,740: 18x26
#630 @ 349,411: 19x23
#631 @ 69,800: 12x10
#632 @ 143,278: 22x17
#633 @ 487,186: 28x22
#634 @ 439,941: 12x25
#635 @ 959,694: 11x25
#636 @ 883,360: 25x18
#637 @ 537,120: 20x18
#638 @ 86,41: 22x11
#639 @ 298,685: 18x14
#640 @ 10,424: 28x25
#641 @ 798,213: 26x27
#642 @ 255,310: 13x11
#643 @ 479,147: 11x16
#644 @ 669,48: 11x22
#645 @ 617,118: 16x13
#646 @ 422,668: 29x10
#647 @ 965,684: 18x29
#648 @ 979,543: 10x11
#649 @ 183,142: 26x25
#650 @ 542,979: 21x19
#651 @ 602,26: 25x18
#652 @ 880,160: 15x25
#653 @ 326,571: 23x29
#654 @ 412,81: 12x15
#655 @ 104,713: 24x10
#656 @ 669,526: 27x14
#657 @ 919,733: 18x24
#658 @ 757,307: 15x14
#659 @ 345,79: 17x21
#660 @ 971,343: 25x16
#661 @ 779,902: 29x27
#662 @ 728,519: 23x25
#663 @ 170,323: 16x12
#664 @ 291,926: 10x21
#665 @ 962,159: 26x24
#666 @ 928,162: 16x28
#667 @ 411,76: 15x11
#668 @ 692,422: 10x15
#669 @ 857,798: 26x29
#670 @ 704,143: 28x23
#671 @ 352,319: 16x15
#672 @ 627,827: 21x20
#673 @ 152,807: 14x29
#674 @ 226,414: 16x12
#675 @ 280,917: 16x27
#676 @ 208,905: 23x17
#677 @ 735,440: 16x24
#678 @ 927,983: 27x14
#679 @ 674,121: 25x15
#680 @ 953,811: 22x21
#681 @ 931,714: 20x26
#682 @ 489,520: 28x10
#683 @ 427,159: 16x17
#684 @ 558,972: 18x15
#685 @ 452,364: 19x13
#686 @ 22,553: 24x19
#687 @ 336,676: 23x26
#688 @ 965,415: 24x23
#689 @ 611,777: 14x29
#690 @ 461,50: 22x21
#691 @ 587,749: 18x26
#692 @ 599,860: 21x15
#693 @ 712,677: 11x12
#694 @ 652,179: 18x13
#695 @ 730,922: 24x18
#696 @ 661,672: 11x17
#697 @ 613,539: 17x19
#698 @ 441,607: 20x18
#699 @ 65,249: 26x25
#700 @ 344,682: 27x17
#701 @ 621,271: 29x25
#702 @ 483,51: 28x25
#703 @ 464,613: 15x17
#704 @ 631,469: 10x14
#705 @ 539,317: 21x17
#706 @ 94,878: 10x13
#707 @ 223,645: 16x17
#708 @ 679,428: 12x10
#709 @ 424,254: 13x22
#710 @ 487,45: 22x22
#711 @ 76,428: 8x4
#712 @ 200,272: 26x10
#713 @ 919,179: 23x10
#714 @ 308,503: 13x13
#715 @ 175,655: 11x3
#716 @ 252,519: 27x25
#717 @ 774,26: 24x27
#718 @ 103,867: 13x17
#719 @ 340,527: 16x26
#720 @ 325,79: 27x16
#721 @ 764,772: 12x16
#722 @ 459,496: 19x15
#723 @ 682,428: 27x14
#724 @ 77,796: 11x26
#725 @ 773,156: 16x23
#726 @ 687,242: 16x11
#727 @ 336,579: 18x27
#728 @ 450,465: 11x13
#729 @ 317,457: 26x25
#730 @ 835,541: 15x23
#731 @ 356,753: 21x23
#732 @ 428,959: 13x21
#733 @ 665,30: 17x22
#734 @ 524,869: 27x10
#735 @ 465,380: 10x15
#736 @ 838,194: 28x27
#737 @ 835,168: 10x16
#738 @ 710,636: 24x28
#739 @ 705,139: 28x14
#740 @ 833,164: 13x11
#741 @ 456,614: 11x25
#742 @ 193,406: 15x18
#743 @ 626,32: 20x23
#744 @ 846,109: 19x29
#745 @ 175,674: 15x13
#746 @ 280,127: 27x17
#747 @ 784,540: 11x13
#748 @ 102,387: 20x27
#749 @ 206,381: 14x14
#750 @ 331,697: 16x23
#751 @ 103,869: 10x10
#752 @ 573,553: 19x29
#753 @ 138,781: 22x26
#754 @ 376,597: 20x14
#755 @ 515,897: 11x25
#756 @ 480,121: 23x21
#757 @ 674,671: 24x23
#758 @ 484,47: 28x27
#759 @ 958,804: 20x18
#760 @ 977,36: 17x24
#761 @ 561,34: 26x12
#762 @ 316,276: 18x16
#763 @ 586,33: 17x13
#764 @ 112,368: 26x26
#765 @ 535,935: 10x24
#766 @ 428,381: 22x22
#767 @ 702,117: 13x29
#768 @ 468,503: 15x19
#769 @ 473,375: 11x18
#770 @ 312,43: 29x27
#771 @ 421,617: 23x12
#772 @ 371,986: 21x13
#773 @ 39,731: 25x15
#774 @ 435,914: 12x15
#775 @ 779,873: 10x18
#776 @ 857,510: 22x28
#777 @ 595,275: 24x26
#778 @ 601,194: 16x17
#779 @ 532,538: 21x18
#780 @ 626,510: 28x17
#781 @ 151,915: 20x21
#782 @ 428,455: 23x17
#783 @ 681,767: 19x21
#784 @ 506,311: 19x10
#785 @ 544,939: 14x17
#786 @ 594,440: 19x18
#787 @ 299,868: 17x23
#788 @ 554,880: 11x21
#789 @ 964,312: 14x24
#790 @ 598,429: 22x24
#791 @ 187,970: 26x15
#792 @ 573,347: 23x17
#793 @ 171,476: 23x13
#794 @ 359,748: 27x18
#795 @ 28,418: 11x16
#796 @ 937,873: 24x20
#797 @ 722,669: 10x11
#798 @ 213,537: 25x18
#799 @ 490,295: 15x10
#800 @ 620,562: 24x14
#801 @ 444,365: 13x27
#802 @ 395,757: 28x28
#803 @ 668,335: 23x23
#804 @ 834,479: 26x17
#805 @ 405,88: 16x23
#806 @ 730,287: 22x19
#807 @ 459,661: 5x7
#808 @ 233,849: 18x24
#809 @ 738,18: 25x27
#810 @ 947,268: 24x27
#811 @ 363,983: 24x13
#812 @ 768,384: 23x11
#813 @ 714,790: 26x11
#814 @ 812,447: 15x24
#815 @ 644,667: 21x27
#816 @ 275,575: 26x19
#817 @ 746,759: 19x16
#818 @ 550,130: 16x20
#819 @ 842,662: 21x18
#820 @ 937,425: 23x29
#821 @ 142,152: 13x19
#822 @ 254,911: 26x28
#823 @ 36,411: 24x20
#824 @ 701,625: 18x25
#825 @ 535,878: 22x12
#826 @ 427,251: 23x16
#827 @ 391,255: 24x12
#828 @ 181,386: 20x18
#829 @ 829,352: 21x13
#830 @ 528,502: 13x26
#831 @ 819,673: 12x20
#832 @ 49,255: 18x10
#833 @ 172,312: 11x20
#834 @ 743,415: 18x24
#835 @ 584,773: 23x23
#836 @ 841,188: 14x25
#837 @ 65,531: 12x16
#838 @ 890,572: 11x12
#839 @ 598,845: 28x18
#840 @ 766,514: 17x20
#841 @ 502,706: 25x26
#842 @ 382,833: 28x21
#843 @ 91,762: 17x17
#844 @ 349,8: 18x13
#845 @ 331,743: 27x15
#846 @ 585,786: 10x27
#847 @ 830,826: 29x27
#848 @ 352,757: 10x23
#849 @ 765,248: 27x12
#850 @ 707,117: 13x4
#851 @ 547,804: 13x16
#852 @ 333,386: 21x14
#853 @ 12,499: 29x15
#854 @ 103,810: 12x28
#855 @ 413,731: 20x26
#856 @ 798,169: 12x15
#857 @ 731,597: 19x23
#858 @ 778,28: 12x19
#859 @ 174,856: 18x16
#860 @ 408,194: 3x5
#861 @ 563,579: 25x14
#862 @ 395,760: 17x29
#863 @ 793,927: 20x27
#864 @ 621,378: 17x14
#865 @ 962,124: 23x11
#866 @ 200,488: 16x15
#867 @ 26,718: 7x4
#868 @ 34,106: 13x27
#869 @ 103,822: 13x24
#870 @ 902,167: 12x20
#871 @ 818,443: 15x24
#872 @ 305,640: 14x10
#873 @ 688,17: 10x17
#874 @ 436,775: 19x27
#875 @ 610,723: 27x27
#876 @ 51,620: 22x28
#877 @ 285,686: 29x11
#878 @ 765,469: 20x29
#879 @ 603,387: 3x8
#880 @ 13,323: 16x10
#881 @ 942,327: 22x20
#882 @ 324,864: 10x12
#883 @ 757,382: 24x25
#884 @ 460,736: 11x16
#885 @ 911,143: 20x19
#886 @ 881,936: 16x25
#887 @ 521,104: 28x10
#888 @ 968,512: 26x24
#889 @ 283,862: 17x15
#890 @ 176,501: 24x27
#891 @ 191,789: 27x20
#892 @ 96,466: 27x23
#893 @ 485,242: 23x12
#894 @ 531,959: 3x6
#895 @ 172,627: 18x29
#896 @ 446,724: 24x14
#897 @ 62,545: 15x23
#898 @ 833,588: 27x14
#899 @ 613,86: 25x16
#900 @ 697,709: 23x18
#901 @ 62,420: 15x19
#902 @ 375,537: 12x16
#903 @ 283,256: 28x16
#904 @ 173,733: 29x27
#905 @ 386,357: 20x19
#906 @ 272,39: 25x19
#907 @ 3,496: 14x23
#908 @ 335,591: 25x29
#909 @ 607,724: 20x18
#910 @ 349,313: 26x26
#911 @ 258,312: 13x22
#912 @ 598,180: 29x20
#913 @ 220,768: 24x22
#914 @ 861,30: 28x21
#915 @ 722,893: 24x13
#916 @ 32,911: 21x15
#917 @ 64,677: 4x5
#918 @ 825,597: 12x29
#919 @ 221,194: 23x29
#920 @ 678,658: 28x17
#921 @ 506,601: 14x29
#922 @ 633,892: 16x10
#923 @ 788,473: 25x17
#924 @ 923,393: 22x23
#925 @ 421,770: 18x15
#926 @ 746,530: 17x26
#927 @ 114,370: 11x15
#928 @ 43,550: 24x27
#929 @ 608,91: 22x21
#930 @ 569,963: 26x29
#931 @ 192,155: 11x23
#932 @ 579,599: 21x15
#933 @ 864,688: 20x11
#934 @ 653,878: 13x27
#935 @ 786,513: 12x13
#936 @ 694,784: 28x17
#937 @ 356,87: 27x23
#938 @ 814,881: 10x15
#939 @ 380,177: 25x20
#940 @ 406,119: 23x12
#941 @ 881,595: 13x15
#942 @ 241,89: 27x28
#943 @ 282,306: 24x17
#944 @ 884,176: 25x10
#945 @ 255,230: 16x23
#946 @ 908,555: 19x25
#947 @ 268,8: 15x26
#948 @ 547,553: 23x18
#949 @ 366,807: 17x21
#950 @ 318,514: 24x13
#951 @ 389,659: 19x28
#952 @ 888,162: 20x18
#953 @ 183,290: 18x18
#954 @ 457,657: 13x20
#955 @ 398,656: 27x18
#956 @ 326,900: 25x21
#957 @ 328,0: 29x14
#958 @ 427,952: 14x23
#959 @ 928,408: 19x20
#960 @ 451,553: 22x24
#961 @ 31,617: 18x19
#962 @ 88,657: 24x20
#963 @ 772,938: 19x14
#964 @ 46,387: 16x28
#965 @ 648,905: 26x25
#966 @ 499,741: 21x27
#967 @ 725,290: 27x22
#968 @ 338,686: 22x26
#969 @ 919,982: 14x13
#970 @ 322,413: 14x19
#971 @ 313,950: 13x18
#972 @ 129,845: 28x15
#973 @ 826,372: 27x28
#974 @ 463,529: 21x13
#975 @ 577,187: 22x29
#976 @ 556,888: 18x13
#977 @ 591,784: 29x19
#978 @ 912,23: 16x14
#979 @ 360,774: 13x17
#980 @ 513,315: 10x29
#981 @ 147,898: 10x25
#982 @ 24,715: 17x14
#983 @ 803,917: 26x27
#984 @ 769,368: 17x6
#985 @ 546,842: 18x24
#986 @ 132,328: 13x19
#987 @ 235,444: 23x27
#988 @ 399,736: 22x25
#989 @ 159,793: 22x22
#990 @ 297,351: 26x15
#991 @ 650,0: 13x29
#992 @ 534,516: 17x14
#993 @ 839,180: 17x15
#994 @ 853,167: 25x13
#995 @ 591,621: 21x18
#996 @ 511,557: 19x27
#997 @ 637,880: 23x25
#998 @ 319,744: 23x14
#999 @ 82,763: 15x25
#1000 @ 830,497: 20x23
#1001 @ 844,669: 10x4
#1002 @ 93,415: 18x10
#1003 @ 662,176: 27x14
#1004 @ 764,290: 19x18
#1005 @ 522,656: 22x18
#1006 @ 577,176: 11x16
#1007 @ 752,346: 11x23
#1008 @ 354,118: 13x21
#1009 @ 617,62: 22x23
#1010 @ 522,707: 20x29
#1011 @ 334,380: 17x18
#1012 @ 194,957: 24x19
#1013 @ 281,790: 26x27
#1014 @ 27,787: 26x15
#1015 @ 418,14: 12x25
#1016 @ 386,818: 15x12
#1017 @ 810,61: 15x25
#1018 @ 456,653: 27x27
#1019 @ 161,161: 10x15
#1020 @ 400,190: 15x18
#1021 @ 743,454: 17x26
#1022 @ 484,668: 15x14
#1023 @ 690,230: 20x28
#1024 @ 294,529: 23x10
#1025 @ 108,318: 29x10
#1026 @ 102,169: 23x22
#1027 @ 199,402: 19x16
#1028 @ 278,271: 15x10
#1029 @ 698,652: 22x16
#1030 @ 159,509: 19x14
#1031 @ 603,429: 19x21
#1032 @ 549,319: 29x26
#1033 @ 332,393: 21x22
#1034 @ 973,431: 10x21
#1035 @ 664,529: 22x24
#1036 @ 719,183: 28x19
#1037 @ 556,333: 16x17
#1038 @ 83,544: 23x10
#1039 @ 50,625: 28x15
#1040 @ 823,229: 29x24
#1041 @ 750,525: 14x20
#1042 @ 823,114: 28x18
#1043 @ 493,130: 24x18
#1044 @ 477,667: 16x17
#1045 @ 446,397: 29x23
#1046 @ 191,475: 23x26
#1047 @ 4,955: 17x16
#1048 @ 982,523: 16x20
#1049 @ 768,516: 8x5
#1050 @ 504,290: 12x17
#1051 @ 666,966: 21x25
#1052 @ 387,968: 26x29
#1053 @ 487,647: 28x24
#1054 @ 326,689: 14x26
#1055 @ 936,939: 29x15
#1056 @ 453,31: 21x22
#1057 @ 419,610: 25x10
#1058 @ 528,107: 12x17
#1059 @ 484,516: 13x17
#1060 @ 575,320: 10x11
#1061 @ 357,467: 28x21
#1062 @ 342,765: 28x18
#1063 @ 620,44: 22x17
#1064 @ 873,567: 20x29
#1065 @ 415,160: 20x25
#1066 @ 469,217: 25x29
#1067 @ 429,645: 18x18
#1068 @ 529,158: 15x16
#1069 @ 680,184: 14x16
#1070 @ 231,790: 24x21
#1071 @ 929,323: 25x15
#1072 @ 495,807: 15x25
#1073 @ 263,256: 15x10
#1074 @ 796,784: 24x18
#1075 @ 560,886: 13x10
#1076 @ 744,308: 21x26
#1077 @ 752,418: 11x14
#1078 @ 508,724: 10x18
#1079 @ 253,938: 13x19
#1080 @ 790,13: 28x16
#1081 @ 850,179: 13x20
#1082 @ 340,29: 19x26
#1083 @ 909,148: 21x20
#1084 @ 189,921: 11x11
#1085 @ 491,64: 10x20
#1086 @ 660,32: 26x28
#1087 @ 443,211: 14x19
#1088 @ 755,703: 16x5
#1089 @ 519,973: 12x23
#1090 @ 223,928: 21x18
#1091 @ 762,574: 23x24
#1092 @ 827,751: 20x27
#1093 @ 95,393: 13x23
#1094 @ 22,711: 29x18
#1095 @ 774,831: 17x23
#1096 @ 129,519: 15x27
#1097 @ 561,842: 26x13
#1098 @ 312,358: 13x14
#1099 @ 587,263: 14x20
#1100 @ 504,771: 23x21
#1101 @ 684,719: 23x21
#1102 @ 155,509: 29x10
#1103 @ 186,508: 10x9
#1104 @ 181,808: 13x11
#1105 @ 353,61: 17x29
#1106 @ 910,524: 10x17
#1107 @ 385,696: 19x12
#1108 @ 504,390: 28x26
#1109 @ 960,76: 12x26
#1110 @ 758,34: 25x21
#1111 @ 825,836: 15x19
#1112 @ 38,393: 20x11
#1113 @ 248,477: 15x14
#1114 @ 844,541: 18x21
#1115 @ 501,670: 29x10
#1116 @ 245,22: 12x23
#1117 @ 586,393: 13x11
#1118 @ 762,654: 23x28
#1119 @ 656,487: 15x21
#1120 @ 170,783: 27x26
#1121 @ 42,645: 14x13
#1122 @ 424,617: 22x14
#1123 @ 432,658: 12x10
#1124 @ 352,44: 23x18
#1125 @ 492,553: 24x10
#1126 @ 510,583: 25x27
#1127 @ 223,918: 22x23
#1128 @ 580,398: 27x24
#1129 @ 229,382: 10x20
#1130 @ 901,352: 22x23
#1131 @ 697,711: 25x25
#1132 @ 754,635: 26x20
#1133 @ 315,676: 26x16
#1134 @ 931,317: 4x6
#1135 @ 540,1: 10x29
#1136 @ 286,859: 20x22
#1137 @ 938,790: 3x3
#1138 @ 924,76: 21x28
#1139 @ 377,83: 24x28
#1140 @ 182,238: 19x27
#1141 @ 413,732: 20x15
#1142 @ 678,694: 28x15
#1143 @ 549,870: 18x16
#1144 @ 387,774: 12x20
#1145 @ 195,745: 21x26
#1146 @ 155,223: 10x19
#1147 @ 553,522: 28x29
#1148 @ 921,315: 25x11
#1149 @ 909,486: 13x25
#1150 @ 415,702: 27x25
#1151 @ 829,349: 13x15
#1152 @ 694,682: 29x22
#1153 @ 951,876: 6x12
#1154 @ 629,830: 25x26
#1155 @ 27,922: 16x10
#1156 @ 107,819: 16x29
#1157 @ 471,978: 27x14
#1158 @ 487,690: 16x29
#1159 @ 701,182: 24x13
#1160 @ 240,881: 16x28
#1161 @ 497,551: 11x15
#1162 @ 467,229: 17x27
#1163 @ 726,428: 10x29
#1164 @ 899,86: 19x24
#1165 @ 434,440: 23x12
#1166 @ 313,968: 14x16
#1167 @ 20,96: 25x15
#1168 @ 627,113: 10x18
#1169 @ 335,577: 13x24
#1170 @ 724,724: 16x14
#1171 @ 853,702: 29x10
#1172 @ 501,352: 26x29
#1173 @ 184,152: 14x20
#1174 @ 928,69: 27x13
#1175 @ 597,471: 17x15
#1176 @ 819,670: 12x13
#1177 @ 599,544: 25x25
#1178 @ 959,777: 14x17
#1179 @ 126,906: 10x17
#1180 @ 467,611: 17x11
#1181 @ 180,623: 14x20
#1182 @ 315,51: 26x29
#1183 @ 207,381: 13x25
#1184 @ 108,673: 22x21
#1185 @ 416,947: 15x13
#1186 @ 541,147: 20x20
#1187 @ 848,207: 16x19
#1188 @ 499,168: 18x20
#1189 @ 202,781: 12x12
#1190 @ 743,231: 22x16
#1191 @ 734,912: 19x27
#1192 @ 929,719: 24x18
#1193 @ 961,63: 21x21
#1194 @ 396,591: 13x20
#1195 @ 502,230: 24x28
#1196 @ 349,741: 17x17
#1197 @ 929,772: 22x29
#1198 @ 363,605: 19x12
#1199 @ 609,37: 27x26
#1200 @ 398,207: 22x21
#1201 @ 371,817: 15x22
#1202 @ 886,22: 28x23
#1203 @ 423,654: 18x13
#1204 @ 554,559: 21x21
#1205 @ 241,124: 20x19
#1206 @ 477,146: 28x27
#1207 @ 291,850: 27x12
#1208 @ 193,779: 11x13
#1209 @ 101,844: 20x19
#1210 @ 791,923: 10x11
#1211 @ 511,864: 14x28
#1212 @ 225,400: 23x29
#1213 @ 838,534: 19x13
#1214 @ 724,203: 20x26
#1215 @ 125,343: 21x25
#1216 @ 825,807: 25x23
#1217 @ 189,760: 12x14
#1218 @ 228,689: 13x10
#1219 @ 517,861: 10x18
#1220 @ 90,239: 17x26
#1221 @ 94,405: 16x24
#1222 @ 221,617: 19x21
#1223 @ 104,83: 24x13
#1224 @ 354,600: 13x15
#1225 @ 460,534: 11x22
#1226 @ 360,971: 20x28
#1227 @ 880,246: 23x16
#1228 @ 764,42: 29x18
#1229 @ 411,952: 24x26
#1230 @ 528,956: 18x13
#1231 @ 798,932: 12x29
#1232 @ 376,465: 14x27
#1233 @ 25,316: 17x11
#1234 @ 228,627: 16x20
#1235 @ 152,220: 28x20
#1236 @ 102,44: 21x23
#1237 @ 321,962: 22x25
#1238 @ 27,663: 26x23
#1239 @ 930,86: 19x24
#1240 @ 804,680: 22x17
#1241 @ 343,945: 21x28
#1242 @ 792,499: 10x19
#1243 @ 481,63: 20x15
#1244 @ 655,178: 26x10
#1245 @ 636,33: 25x25
#1246 @ 478,39: 29x17
#1247 @ 439,612: 25x27
#1248 @ 24,203: 27x10
#1249 @ 812,473: 28x15
#1250 @ 892,987: 18x11
#1251 @ 412,438: 26x24
#1252 @ 909,288: 18x21
#1253 @ 612,575: 16x22
#1254 @ 38,417: 20x13
#1255 @ 164,706: 22x17
#1256 @ 168,142: 10x20
#1257 @ 469,138: 15x24
#1258 @ 352,406: 16x18
#1259 @ 539,805: 22x15
#1260 @ 221,626: 15x24
#1261 @ 340,845: 13x24
'''

fl = 1000
fabric = []
for _ in range(fl):
    fabric.append([''] * fl)

rows = inp.strip().split('\n')

for row in rows:
    parts = row.strip().split()
    claim = int(parts[0][1:])
    x, y = [int(c) for c in parts[2][:-1].split(',')]
    dx, dy = [int(p) for p in parts[3].split('x')]
    for i in range(x, x+dx):
        for j in range(y, y+dy):
            if fabric[i][j] is '':
                fabric[i][j] = claim
            else:
                fabric[i][j] = -1

count = 0
for row in fabric:
    for elem in row:
        if elem == -1:
            count += 1

print count

for row in rows:
    parts = row.strip().split()
    claim = int(parts[0][1:])
    x, y = [int(c) for c in parts[2][:-1].split(',')]
    dx, dy = [int(p) for p in parts[3].split('x')]
    no_overlap = True
    for i in range(x, x+dx):
        for j in range(y, y+dy):
            if fabric[i][j] != claim:
                no_overlap = False
                fabric[i][j] = -1
    if no_overlap:
        print parts

