#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import random
import math

# LINE_OF_POINTS = 10
# NUM_OF_POINTS = 100
# MAP_SIZE = 50.0
# RECEIVE_POINT_NUM = 15
# RECEIVE_THING_NUM = 10

NUM_OF_POINTS = 113

class GENERATOR(object):

    def __init__(self):
        self.x = []
        self.y = []
        self.send = []
        self.receive = []

    def generate_point(self,point_file,start,end_information):

        f = open(point_file,'w') # clean up the file
        f.truncate()
        f.close()

        f = open(point_file,'a')

        for i in range(NUM_OF_POINTS):
            if i in end_information.keys():
                self.receive.append(end_information[i])
            else:
                self.receive.append(0)

        send = sum(self.receive)

        for i in range(NUM_OF_POINTS):
            if i == start:
                self.send.append(send)
            else:
                self.send.append(0)

        # example = random.sample(range(NUM_OF_POINTS),RECEIVE_POINT_NUM+1) # random send/receive point ID
        #
        # for i in range(NUM_OF_POINTS): # random send num
        #     if i in example[1:RECEIVE_POINT_NUM+1]:
        #         receive = random.randint(1,RECEIVE_THING_NUM)
        #         self.receive.append(receive)
        #     else:
        #         self.receive.append(0)
        #
        # send = sum(self.receive) # calculate receive num
        # for i in range(NUM_OF_POINTS):
        #     if i==example[0]:
        #         self.send.append(send)
        #     else:
        #         self.send.append(0)



        # for i in range(NUM_OF_POINTS):
        #     x_sand = i % LINE_OF_POINTS + 1 # x
        #     x = random.uniform(x_sand * MAP_SIZE - 5.0, x_sand * MAP_SIZE + 5.0)
        #     y_sand = i // LINE_OF_POINTS + 1 # y
        #     y = random.uniform(y_sand * MAP_SIZE - 5.0, y_sand * MAP_SIZE + 5.0)
        #     self.x.append(x)
        #     self.y.append(y)
        #
        #     result = str(x) + " " + str(y) + " " + str(self.send[i]) + " " + str(self.receive[i])
        #     f.write(result+"\n")

        self.x.append(118954688) #0
        self.y.append(32116967)
        self.x.append(118954806)
        self.y.append(32117008)
        self.x.append(118955621)
        self.y.append(32117290)
        self.x.append(118956179)
        self.y.append(32117467)
        self.x.append(118956292)
        self.y.append(32116931)
        self.x.append(118956581)
        self.y.append(32116617)
        self.x.append(118956045)
        self.y.append(32116426)
        self.x.append(118955219)
        self.y.append(32116213)
        self.x.append(118955096)
        self.y.append(32116167)
        self.x.append(118955745)
        self.y.append(32114904)
        self.x.append(118955868)  #10
        self.y.append(32114950)
        self.x.append(118956206)
        self.y.append(32116122)
        self.x.append(118955718)
        self.y.append(32115908)
        self.x.append(118956871)
        self.y.append(32116481)
        self.x.append(118956619)
        self.y.append(32116245)
        self.x.append(118956388)
        self.y.append(32115768)
        self.x.append(118955777)
        self.y.append(32115568)
        self.x.append(118956544)
        self.y.append(32115440)
        self.x.append(118956007)
        self.y.append(32115277)
        self.x.append(118956614)
        self.y.append(32115295)
        self.x.append(118956651)  #20
        self.y.append(32115209)
        self.x.append(118956683)
        self.y.append(32115150)
        self.x.append(118956694)
        self.y.append(32115918)
        self.x.append(118957209)
        self.y.append(32116326)
        self.x.append(118957590)
        self.y.append(32116149)
        self.x.append(118957311)
        self.y.append(32115868)
        self.x.append(118956973)
        self.y.append(32115631)
        self.x.append(118957107)
        self.y.append(32115440)
        self.x.append(118957853)
        self.y.append(32116027)
        self.x.append(118958003)
        self.y.append(32115936)
        self.x.append(118957214)  #30
        self.y.append(32115318)
        self.x.append(118958266)
        self.y.append(32115849)
        self.x.append(118957746)
        self.y.append(32115395)
        self.x.append(118956871)
        self.y.append(32114754)
        self.x.append(118957375)
        self.y.append(32114959)
        self.x.append(118956324)
        self.y.append(32114623)
        self.x.append(118957134)
        self.y.append(32114255)
        self.x.append(118956522)
        self.y.append(32113755)
        self.x.append(118956431)
        self.y.append(32113687)
        self.x.append(118956174)
        self.y.append(32113559)
        self.x.append(118955439)  #40
        self.y.append(32113296)
        self.x.append(118955476)
        self.y.append(32112982)
        self.x.append(118956335)
        self.y.append(32113378)
        self.x.append(118956544)
        self.y.append(32113228)
        self.x.append(118957011)
        self.y.append(32113005)
        self.x.append(118957145)
        self.y.append(32112951)
        self.x.append(118957241)
        self.y.append(32113069)
        self.x.append(118957300)
        self.y.append(32113173)
        self.x.append(118958346)
        self.y.append(32112896)
        self.x.append(118958357)
        self.y.append(32112787)
        self.x.append(118958502)  #50
        self.y.append(32113278)
        self.x.append(118957365)
        self.y.append(32113541)
        self.x.append(118956930)
        self.y.append(32113882)
        self.x.append(118958754)
        self.y.append(32114068)
        self.x.append(118958191)
        self.y.append(32114150)
        self.x.append(118957574)
        self.y.append(32114614)
        self.x.append(118958019)
        self.y.append(32114995)
        self.x.append(118958877)
        self.y.append(32114745)
        self.x.append(118959108)
        self.y.append(32114082)
        self.x.append(118959199)
        self.y.append(32113373)
        self.x.append(118959881)  #60
        self.y.append(32113478)
        self.x.append(118960047)
        self.y.append(32113082)
        self.x.append(118960079)
        self.y.append(32112996)
        self.x.append(118960315)
        self.y.append(32113023)
        self.x.append(118960283)
        self.y.append(32113155)
        self.x.append(118960514)
        self.y.append(32113060)
        self.x.append(118960642)
        self.y.append(32113191)
        self.x.append(118960551)
        self.y.append(32113564)
        self.x.append(118960921)
        self.y.append(32113673)
        self.x.append(118960664)
        self.y.append(32114795)
        self.x.append(118960224)  #70
        self.y.append(32114677)
        self.x.append(118959312)
        self.y.append(32114536)
        self.x.append(118960186)
        self.y.append(32114895)
        self.x.append(118960852)
        self.y.append(32115004)
        self.x.append(118960793)
        self.y.append(32115427)
        self.x.append(118959146)
        self.y.append(32115241)
        self.x.append(118961190)
        self.y.append(32115059)
        self.x.append(118960948)
        self.y.append(32115459)
        self.x.append(118962241)
        self.y.append(32113310)
        self.x.append(118962187)
        self.y.append(32113423)
        self.x.append(118961651)  #80
        self.y.append(32114318)
        self.x.append(118962793)
        self.y.append(32114591)
        self.x.append(118962531)
        self.y.append(32115286)
        self.x.append(118961329)
        self.y.append(32114850)
        self.x.append(118962091)
        self.y.append(32115281)
        self.x.append(118961141)
        self.y.append(32115168)
        self.x.append(118962021)
        self.y.append(32115890)
        self.x.append(118961517)
        self.y.append(32115868)
        self.x.append(118960846)
        self.y.append(32115799)
        self.x.append(118960771)
        self.y.append(32115913)
        self.x.append(118961485)  #90
        self.y.append(32116018)
        self.x.append(118961597)
        self.y.append(32116063)
        self.x.append(118961597)
        self.y.append(32116485)
        self.x.append(118961082)
        self.y.append(32116840)
        self.x.append(118960948)
        self.y.append(32116949)
        self.x.append(118960852)
        self.y.append(32117226)
        self.x.append(118960524)
        self.y.append(32117399)
        self.x.append(118959714)
        self.y.append(32116713)
        self.x.append(118960396)
        self.y.append(32116167)
        self.x.append(118960369)
        self.y.append(32115877)
        self.x.append(118960385)  #100
        self.y.append(32115718)
        self.x.append(118959425)
        self.y.append(32115622)
        self.x.append(118958835)
        self.y.append(32115686)
        self.x.append(118959569)
        self.y.append(32115754)
        self.x.append(118959258)
        self.y.append(32115986)
        self.x.append(118959430)
        self.y.append(32116195)
        self.x.append(118959339)
        self.y.append(32116349)
        self.x.append(118959414)
        self.y.append(32116917)
        self.x.append(118959387)
        self.y.append(32117294)
        self.x.append(118959199)
        self.y.append(32117276)
        self.x.append(118958405) #110
        self.y.append(32116554)
        self.x.append(118959108)
        self.y.append(32116027)
        self.x.append(118957611)
        self.y.append(32116485)

        for i in range(NUM_OF_POINTS):
            f.write(str(self.x[i]) + " " + str(self.y[i]) + " " + str(self.send[i]) + " " + str(self.receive[i]) + "\n")

        f.close()

    def generate_line(self,line_file):
        f = open(line_file, 'w') # clean up the file
        f.truncate()
        f.close()

        f = open(line_file,'a')

        # for i in range(NUM_OF_POINTS):
        #     if i % LINE_OF_POINTS != (LINE_OF_POINTS-1): # start and end in row
        #         start = i
        #         end = start + 1
        #         distance = math.sqrt((self.x[start]-self.x[end])**2+(self.y[start]-self.y[end])**2)
        #         cost = random.uniform(distance-5.0,distance+5.0)
        #         f.write(str(start) + " " + str(end) + " " + str(cost) + "\n")
        #     if i // LINE_OF_POINTS != (LINE_OF_POINTS-1): # start and end in col
        #         start = i
        #         end = start + LINE_OF_POINTS
        #         distance = math.sqrt((self.x[start] - self.x[end]) ** 2 + (self.y[start] - self.y[end]) ** 2)
        #         cost = random.uniform(distance-5.0,distance+5.0)
        #         f.write(str(start) + " " + str(end) + " " + str(cost) + "\n")

        f.write(str(0) + " " + str(1) + " " + str(
            math.sqrt(pow(self.x[0] - self.x[1], 2) + pow(self.y[0] - self.y[1], 2))) + "\n")
        f.write(str(0) + " " + str(8) + " " + str(
            math.sqrt(pow(self.x[0] - self.x[8], 2) + pow(self.y[0] - self.y[8], 2))) + "\n")
        f.write(str(1) + " " + str(2) + " " + str(
            math.sqrt(pow(self.x[1] - self.x[2], 2) + pow(self.y[1] - self.y[2], 2))) + "\n")
        f.write(str(1) + " " + str(7) + " " + str(
            math.sqrt(pow(self.x[1] - self.x[7], 2) + pow(self.y[1] - self.y[7], 2))) + "\n")
        f.write(str(2) + " " + str(3) + " " + str(
            math.sqrt(pow(self.x[2] - self.x[3], 2) + pow(self.y[2] - self.y[3], 2))) + "\n")
        f.write(str(2) + " " + str(6) + " " + str(
            math.sqrt(pow(self.x[2] - self.x[6], 2) + pow(self.y[2] - self.y[6], 2))) + "\n")
        f.write(str(3) + " " + str(4) + " " + str(
            math.sqrt(pow(self.x[3] - self.x[4], 2) + pow(self.y[3] - self.y[4], 2))) + "\n")
        f.write(str(4) + " " + str(5) + " " + str(
            math.sqrt(pow(self.x[4] - self.x[5], 2) + pow(self.y[4] - self.y[5], 2))) + "\n")
        f.write(str(5) + " " + str(6) + " " + str(
            math.sqrt(pow(self.x[5] - self.x[6], 2) + pow(self.y[5] - self.y[6], 2))) + "\n")
        f.write(str(5) + " " + str(13) + " " + str(
            math.sqrt(pow(self.x[5] - self.x[13], 2) + pow(self.y[5] - self.y[13], 2))) + "\n")
        f.write(str(6) + " " + str(7) + " " + str(
            math.sqrt(pow(self.x[6] - self.x[7], 2) + pow(self.y[6] - self.y[7], 2))) + "\n")
        f.write(str(6) + " " + str(11) + " " + str(
            math.sqrt(pow(self.x[6] - self.x[11], 2) + pow(self.y[6] - self.y[11], 2))) + "\n")
        f.write(str(7) + " " + str(8) + " " + str(
            math.sqrt(pow(self.x[7] - self.x[8], 2) + pow(self.y[7] - self.y[8], 2))) + "\n")
        f.write(str(7) + " " + str(10) + " " + str(
            math.sqrt(pow(self.x[7] - self.x[10], 2) + pow(self.y[7] - self.y[10], 2))) + "\n")
        f.write(str(8) + " " + str(9) + " " + str(
            math.sqrt(pow(self.x[8] - self.x[9], 2) + pow(self.y[8] - self.y[9], 2))) + "\n")
        f.write(str(9) + " " + str(10) + " " + str(
            math.sqrt(pow(self.x[9] - self.x[10], 2) + pow(self.y[9] - self.y[10], 2))) + "\n")
        f.write(str(9) + " " + str(38) + " " + str(
            math.sqrt(pow(self.x[9] - self.x[38], 2) + pow(self.y[9] - self.y[38], 2))) + "\n")
        f.write(str(10) + " " + str(20) + " " + str(
            math.sqrt(pow(self.x[10] - self.x[20], 2) + pow(self.y[10] - self.y[20], 2))) + "\n")
        f.write(str(10) + " " + str(37) + " " + str(
            math.sqrt(pow(self.x[10] - self.x[37], 2) + pow(self.y[10] - self.y[37], 2))) + "\n")
        f.write(str(11) + " " + str(12) + " " + str(
            math.sqrt(pow(self.x[11] - self.x[12], 2) + pow(self.y[11] - self.y[12], 2))) + "\n")
        f.write(str(11) + " " + str(15) + " " + str(
            math.sqrt(pow(self.x[11] - self.x[15], 2) + pow(self.y[11] - self.y[15], 2))) + "\n")
        f.write(str(13) + " " + str(14) + " " + str(
            math.sqrt(pow(self.x[13] - self.x[14], 2) + pow(self.y[13] - self.y[14], 2))) + "\n")
        f.write(str(13) + " " + str(23) + " " + str(
            math.sqrt(pow(self.x[13] - self.x[23], 2) + pow(self.y[13] - self.y[23], 2))) + "\n")
        f.write(str(15) + " " + str(16) + " " + str(
            math.sqrt(pow(self.x[15] - self.x[16], 2) + pow(self.y[15] - self.y[16], 2))) + "\n")
        f.write(str(15) + " " + str(17) + " " + str(
            math.sqrt(pow(self.x[15] - self.x[17], 2) + pow(self.y[15] - self.y[17], 2))) + "\n")
        f.write(str(15) + " " + str(22) + " " + str(
            math.sqrt(pow(self.x[15] - self.x[22], 2) + pow(self.y[15] - self.y[22], 2))) + "\n")
        f.write(str(17) + " " + str(18) + " " + str(
            math.sqrt(pow(self.x[17] - self.x[18], 2) + pow(self.y[17] - self.y[18], 2))) + "\n")
        f.write(str(17) + " " + str(19) + " " + str(
            math.sqrt(pow(self.x[17] - self.x[19], 2) + pow(self.y[17] - self.y[19], 2))) + "\n")
        f.write(str(17) + " " + str(26) + " " + str(
            math.sqrt(pow(self.x[17] - self.x[26], 2) + pow(self.y[17] - self.y[26], 2))) + "\n")
        f.write(str(19) + " " + str(20) + " " + str(
            math.sqrt(pow(self.x[19] - self.x[20], 2) + pow(self.y[19] - self.y[20], 2))) + "\n")
        f.write(str(19) + " " + str(27) + " " + str(
            math.sqrt(pow(self.x[19] - self.x[27], 2) + pow(self.y[19] - self.y[27], 2))) + "\n")
        f.write(str(20) + " " + str(21) + " " + str(
            math.sqrt(pow(self.x[20] - self.x[21], 2) + pow(self.y[20] - self.y[21], 2))) + "\n")
        f.write(str(21) + " " + str(30) + " " + str(
            math.sqrt(pow(self.x[21] - self.x[30], 2) + pow(self.y[21] - self.y[30], 2))) + "\n")
        f.write(str(21) + " " + str(33) + " " + str(
            math.sqrt(pow(self.x[21] - self.x[33], 2) + pow(self.y[21] - self.y[33], 2))) + "\n")
        f.write(str(22) + " " + str(23) + " " + str(
            math.sqrt(pow(self.x[22] - self.x[23], 2) + pow(self.y[22] - self.y[23], 2))) + "\n")
        f.write(str(23) + " " + str(24) + " " + str(
            math.sqrt(pow(self.x[23] - self.x[24], 2) + pow(self.y[23] - self.y[24], 2))) + "\n")
        f.write(str(23) + " " + str(112) + " " + str(
            math.sqrt(pow(self.x[23] - self.x[112], 2) + pow(self.y[23] - self.y[112], 2))) + "\n")
        f.write(str(24) + " " + str(25) + " " + str(
            math.sqrt(pow(self.x[24] - self.x[25], 2) + pow(self.y[24] - self.y[25], 2))) + "\n")
        f.write(str(24) + " " + str(28) + " " + str(
            math.sqrt(pow(self.x[24] - self.x[28], 2) + pow(self.y[24] - self.y[28], 2))) + "\n")
        f.write(str(27) + " " + str(28) + " " + str(
            math.sqrt(pow(self.x[27] - self.x[28], 2) + pow(self.y[27] - self.y[28], 2))) + "\n")
        f.write(str(28) + " " + str(29) + " " + str(
            math.sqrt(pow(self.x[28] - self.x[29], 2) + pow(self.y[28] - self.y[29], 2))) + "\n")
        f.write(str(29) + " " + str(30) + " " + str(
            math.sqrt(pow(self.x[29] - self.x[30], 2) + pow(self.y[29] - self.y[30], 2))) + "\n")
        f.write(str(29) + " " + str(31) + " " + str(
            math.sqrt(pow(self.x[29] - self.x[31], 2) + pow(self.y[29] - self.y[31], 2))) + "\n")
        f.write(str(31) + " " + str(32) + " " + str(
            math.sqrt(pow(self.x[31] - self.x[32], 2) + pow(self.y[31] - self.y[32], 2))) + "\n")
        f.write(str(31) + " " + str(102) + " " + str(
            math.sqrt(pow(self.x[31] - self.x[102], 2) + pow(self.y[31] - self.y[102], 2))) + "\n")
        f.write(str(33) + " " + str(34) + " " + str(
            math.sqrt(pow(self.x[33] - self.x[34], 2) + pow(self.y[33] - self.y[34], 2))) + "\n")
        f.write(str(33) + " " + str(35) + " " + str(
            math.sqrt(pow(self.x[33] - self.x[35], 2) + pow(self.y[33] - self.y[35], 2))) + "\n")
        f.write(str(33) + " " + str(36) + " " + str(
            math.sqrt(pow(self.x[33] - self.x[36], 2) + pow(self.y[33] - self.y[36], 2))) + "\n")
        f.write(str(36) + " " + str(37) + " " + str(
            math.sqrt(pow(self.x[36] - self.x[37], 2) + pow(self.y[36] - self.y[37], 2))) + "\n")
        f.write(str(36) + " " + str(55) + " " + str(
            math.sqrt(pow(self.x[36] - self.x[55], 2) + pow(self.y[36] - self.y[55], 2))) + "\n")
        f.write(str(37) + " " + str(38) + " " + str(
            math.sqrt(pow(self.x[37] - self.x[38], 2) + pow(self.y[37] - self.y[38], 2))) + "\n")
        f.write(str(37) + " " + str(47) + " " + str(
            math.sqrt(pow(self.x[37] - self.x[47], 2) + pow(self.y[37] - self.y[47], 2))) + "\n")
        f.write(str(38) + " " + str(39) + " " + str(
            math.sqrt(pow(self.x[38] - self.x[39], 2) + pow(self.y[38] - self.y[39], 2))) + "\n")
        f.write(str(38) + " " + str(46) + " " + str(
            math.sqrt(pow(self.x[38] - self.x[46], 2) + pow(self.y[38] - self.y[46], 2))) + "\n")
        f.write(str(39) + " " + str(40) + " " + str(
            math.sqrt(pow(self.x[39] - self.x[40], 2) + pow(self.y[39] - self.y[40], 2))) + "\n")
        f.write(str(39) + " " + str(42) + " " + str(
            math.sqrt(pow(self.x[39] - self.x[42], 2) + pow(self.y[39] - self.y[42], 2))) + "\n")
        f.write(str(40) + " " + str(41) + " " + str(
            math.sqrt(pow(self.x[40] - self.x[41], 2) + pow(self.y[40] - self.y[41], 2))) + "\n")
        f.write(str(41) + " " + str(42) + " " + str(
            math.sqrt(pow(self.x[41] - self.x[42], 2) + pow(self.y[41] - self.y[42], 2))) + "\n")
        f.write(str(42) + " " + str(43) + " " + str(
            math.sqrt(pow(self.x[42] - self.x[43], 2) + pow(self.y[42] - self.y[43], 2))) + "\n")
        f.write(str(43) + " " + str(44) + " " + str(
            math.sqrt(pow(self.x[43] - self.x[44], 2) + pow(self.y[43] - self.y[44], 2))) + "\n")
        f.write(str(44) + " " + str(45) + " " + str(
            math.sqrt(pow(self.x[44] - self.x[45], 2) + pow(self.y[44] - self.y[45], 2))) + "\n")
        f.write(str(45) + " " + str(46) + " " + str(
            math.sqrt(pow(self.x[45] - self.x[46], 2) + pow(self.y[45] - self.y[46], 2))) + "\n")
        f.write(str(46) + " " + str(47) + " " + str(
            math.sqrt(pow(self.x[46] - self.x[47], 2) + pow(self.y[46] - self.y[47], 2))) + "\n")
        f.write(str(46) + " " + str(49) + " " + str(
            math.sqrt(pow(self.x[46] - self.x[49], 2) + pow(self.y[46] - self.y[49], 2))) + "\n")
        f.write(str(47) + " " + str(48) + " " + str(
            math.sqrt(pow(self.x[47] - self.x[48], 2) + pow(self.y[47] - self.y[48], 2))) + "\n")
        f.write(str(48) + " " + str(49) + " " + str(
            math.sqrt(pow(self.x[48] - self.x[49], 2) + pow(self.y[48] - self.y[49], 2))) + "\n")
        f.write(str(48) + " " + str(50) + " " + str(
            math.sqrt(pow(self.x[48] - self.x[50], 2) + pow(self.y[48] - self.y[50], 2))) + "\n")
        f.write(str(48) + " " + str(61) + " " + str(
            math.sqrt(pow(self.x[48] - self.x[61], 2) + pow(self.y[48] - self.y[61], 2))) + "\n")
        f.write(str(49) + " " + str(62) + " " + str(
            math.sqrt(pow(self.x[49] - self.x[62], 2) + pow(self.y[49] - self.y[62], 2))) + "\n")
        f.write(str(50) + " " + str(51) + " " + str(
            math.sqrt(pow(self.x[50] - self.x[51], 2) + pow(self.y[50] - self.y[51], 2))) + "\n")
        f.write(str(50) + " " + str(53) + " " + str(
            math.sqrt(pow(self.x[50] - self.x[53], 2) + pow(self.y[50] - self.y[53], 2))) + "\n")
        f.write(str(50) + " " + str(59) + " " + str(
            math.sqrt(pow(self.x[50] - self.x[59], 2) + pow(self.y[50] - self.y[59], 2))) + "\n")
        f.write(str(51) + " " + str(52) + " " + str(
            math.sqrt(pow(self.x[51] - self.x[52], 2) + pow(self.y[51] - self.y[52], 2))) + "\n")
        f.write(str(53) + " " + str(54) + " " + str(
            math.sqrt(pow(self.x[53] - self.x[54], 2) + pow(self.y[53] - self.y[54], 2))) + "\n")
        f.write(str(53) + " " + str(58) + " " + str(
            math.sqrt(pow(self.x[53] - self.x[58], 2) + pow(self.y[53] - self.y[58], 2))) + "\n")
        f.write(str(54) + " " + str(55) + " " + str(
            math.sqrt(pow(self.x[54] - self.x[55], 2) + pow(self.y[54] - self.y[55], 2))) + "\n")
        f.write(str(55) + " " + str(56) + " " + str(
            math.sqrt(pow(self.x[55] - self.x[56], 2) + pow(self.y[55] - self.y[56], 2))) + "\n")
        f.write(str(56) + " " + str(57) + " " + str(
            math.sqrt(pow(self.x[56] - self.x[57], 2) + pow(self.y[56] - self.y[57], 2))) + "\n")
        f.write(str(56) + " " + str(102) + " " + str(
            math.sqrt(pow(self.x[56] - self.x[102], 2) + pow(self.y[56] - self.y[102], 2))) + "\n")
        f.write(str(57) + " " + str(58) + " " + str(
            math.sqrt(pow(self.x[57] - self.x[58], 2) + pow(self.y[57] - self.y[58], 2))) + "\n")
        f.write(str(57) + " " + str(72) + " " + str(
            math.sqrt(pow(self.x[57] - self.x[72], 2) + pow(self.y[57] - self.y[72], 2))) + "\n")
        f.write(str(58) + " " + str(59) + " " + str(
            math.sqrt(pow(self.x[58] - self.x[59], 2) + pow(self.y[58] - self.y[59], 2))) + "\n")
        f.write(str(59) + " " + str(60) + " " + str(
            math.sqrt(pow(self.x[59] - self.x[60], 2) + pow(self.y[59] - self.y[60], 2))) + "\n")
        f.write(str(60) + " " + str(61) + " " + str(
            math.sqrt(pow(self.x[60] - self.x[61], 2) + pow(self.y[60] - self.y[61], 2))) + "\n")
        f.write(str(60) + " " + str(67) + " " + str(
            math.sqrt(pow(self.x[60] - self.x[67], 2) + pow(self.y[60] - self.y[67], 2))) + "\n")
        f.write(str(61) + " " + str(62) + " " + str(
            math.sqrt(pow(self.x[61] - self.x[62], 2) + pow(self.y[61] - self.y[62], 2))) + "\n")
        f.write(str(61) + " " + str(64) + " " + str(
            math.sqrt(pow(self.x[61] - self.x[64], 2) + pow(self.y[61] - self.y[64], 2))) + "\n")
        f.write(str(62) + " " + str(63) + " " + str(
            math.sqrt(pow(self.x[62] - self.x[63], 2) + pow(self.y[62] - self.y[63], 2))) + "\n")
        f.write(str(63) + " " + str(64) + " " + str(
            math.sqrt(pow(self.x[63] - self.x[64], 2) + pow(self.y[63] - self.y[64], 2))) + "\n")
        f.write(str(63) + " " + str(65) + " " + str(
            math.sqrt(pow(self.x[63] - self.x[65], 2) + pow(self.y[63] - self.y[65], 2))) + "\n")
        f.write(str(64) + " " + str(66) + " " + str(
            math.sqrt(pow(self.x[64] - self.x[66], 2) + pow(self.y[64] - self.y[66], 2))) + "\n")
        f.write(str(65) + " " + str(78) + " " + str(
            math.sqrt(pow(self.x[65] - self.x[78], 2) + pow(self.y[65] - self.y[78], 2))) + "\n")
        f.write(str(66) + " " + str(67) + " " + str(
            math.sqrt(pow(self.x[66] - self.x[67], 2) + pow(self.y[66] - self.y[67], 2))) + "\n")
        f.write(str(66) + " " + str(79) + " " + str(
            math.sqrt(pow(self.x[66] - self.x[79], 2) + pow(self.y[66] - self.y[79], 2))) + "\n")
        f.write(str(67) + " " + str(68) + " " + str(
            math.sqrt(pow(self.x[67] - self.x[68], 2) + pow(self.y[67] - self.y[68], 2))) + "\n")
        f.write(str(68) + " " + str(69) + " " + str(
            math.sqrt(pow(self.x[68] - self.x[69], 2) + pow(self.y[68] - self.y[69], 2))) + "\n")
        f.write(str(69) + " " + str(70) + " " + str(
            math.sqrt(pow(self.x[69] - self.x[70], 2) + pow(self.y[69] - self.y[70], 2))) + "\n")
        f.write(str(70) + " " + str(71) + " " + str(
            math.sqrt(pow(self.x[70] - self.x[71], 2) + pow(self.y[70] - self.y[71], 2))) + "\n")
        f.write(str(70) + " " + str(72) + " " + str(
            math.sqrt(pow(self.x[70] - self.x[72], 2) + pow(self.y[70] - self.y[72], 2))) + "\n")
        f.write(str(72) + " " + str(73) + " " + str(
            math.sqrt(pow(self.x[72] - self.x[73], 2) + pow(self.y[72] - self.y[73], 2))) + "\n")
        f.write(str(73) + " " + str(74) + " " + str(
            math.sqrt(pow(self.x[73] - self.x[74], 2) + pow(self.y[73] - self.y[74], 2))) + "\n")
        f.write(str(73) + " " + str(76) + " " + str(
            math.sqrt(pow(self.x[73] - self.x[76], 2) + pow(self.y[73] - self.y[76], 2))) + "\n")
        f.write(str(74) + " " + str(75) + " " + str(
            math.sqrt(pow(self.x[74] - self.x[75], 2) + pow(self.y[74] - self.y[75], 2))) + "\n")
        f.write(str(74) + " " + str(77) + " " + str(
            math.sqrt(pow(self.x[74] - self.x[77], 2) + pow(self.y[74] - self.y[77], 2))) + "\n")
        f.write(str(76) + " " + str(83) + " " + str(
            math.sqrt(pow(self.x[76] - self.x[83], 2) + pow(self.y[76] - self.y[83], 2))) + "\n")
        f.write(str(76) + " " + str(85) + " " + str(
            math.sqrt(pow(self.x[76] - self.x[85], 2) + pow(self.y[76] - self.y[85], 2))) + "\n")
        f.write(str(77) + " " + str(85) + " " + str(
            math.sqrt(pow(self.x[77] - self.x[85], 2) + pow(self.y[77] - self.y[85], 2))) + "\n")
        f.write(str(77) + " " + str(88) + " " + str(
            math.sqrt(pow(self.x[77] - self.x[88], 2) + pow(self.y[77] - self.y[88], 2))) + "\n")
        f.write(str(78) + " " + str(79) + " " + str(
            math.sqrt(pow(self.x[78] - self.x[79], 2) + pow(self.y[78] - self.y[79], 2))) + "\n")
        f.write(str(79) + " " + str(80) + " " + str(
            math.sqrt(pow(self.x[79] - self.x[80], 2) + pow(self.y[79] - self.y[80], 2))) + "\n")
        f.write(str(80) + " " + str(81) + " " + str(
            math.sqrt(pow(self.x[80] - self.x[81], 2) + pow(self.y[80] - self.y[81], 2))) + "\n")
        f.write(str(80) + " " + str(83) + " " + str(
            math.sqrt(pow(self.x[80] - self.x[83], 2) + pow(self.y[80] - self.y[83], 2))) + "\n")
        f.write(str(81) + " " + str(82) + " " + str(
            math.sqrt(pow(self.x[81] - self.x[82], 2) + pow(self.y[81] - self.y[82], 2))) + "\n")
        f.write(str(82) + " " + str(83) + " " + str(
            math.sqrt(pow(self.x[82] - self.x[83], 2) + pow(self.y[82] - self.y[83], 2))) + "\n")
        f.write(str(82) + " " + str(84) + " " + str(
            math.sqrt(pow(self.x[82] - self.x[84], 2) + pow(self.y[82] - self.y[84], 2))) + "\n")
        f.write(str(84) + " " + str(85) + " " + str(
            math.sqrt(pow(self.x[84] - self.x[85], 2) + pow(self.y[84] - self.y[85], 2))) + "\n")
        f.write(str(84) + " " + str(86) + " " + str(
            math.sqrt(pow(self.x[84] - self.x[86], 2) + pow(self.y[84] - self.y[86], 2))) + "\n")
        f.write(str(86) + " " + str(87) + " " + str(
            math.sqrt(pow(self.x[86] - self.x[87], 2) + pow(self.y[86] - self.y[87], 2))) + "\n")
        f.write(str(87) + " " + str(88) + " " + str(
            math.sqrt(pow(self.x[87] - self.x[88], 2) + pow(self.y[87] - self.y[88], 2))) + "\n")
        f.write(str(87) + " " + str(90) + " " + str(
            math.sqrt(pow(self.x[87] - self.x[90], 2) + pow(self.y[87] - self.y[90], 2))) + "\n")
        f.write(str(88) + " " + str(89) + " " + str(
            math.sqrt(pow(self.x[88] - self.x[89], 2) + pow(self.y[88] - self.y[89], 2))) + "\n")
        f.write(str(88) + " " + str(100) + " " + str(
            math.sqrt(pow(self.x[88] - self.x[100], 2) + pow(self.y[88] - self.y[100], 2))) + "\n")
        f.write(str(89) + " " + str(90) + " " + str(
            math.sqrt(pow(self.x[89] - self.x[90], 2) + pow(self.y[89] - self.y[90], 2))) + "\n")
        f.write(str(89) + " " + str(98) + " " + str(
            math.sqrt(pow(self.x[89] - self.x[98], 2) + pow(self.y[89] - self.y[98], 2))) + "\n")
        f.write(str(90) + " " + str(91) + " " + str(
            math.sqrt(pow(self.x[90] - self.x[91], 2) + pow(self.y[90] - self.y[91], 2))) + "\n")
        f.write(str(91) + " " + str(92) + " " + str(
            math.sqrt(pow(self.x[91] - self.x[92], 2) + pow(self.y[91] - self.y[92], 2))) + "\n")
        f.write(str(92) + " " + str(93) + " " + str(
            math.sqrt(pow(self.x[92] - self.x[93], 2) + pow(self.y[92] - self.y[93], 2))) + "\n")
        f.write(str(93) + " " + str(94) + " " + str(
            math.sqrt(pow(self.x[93] - self.x[94], 2) + pow(self.y[93] - self.y[94], 2))) + "\n")
        f.write(str(93) + " " + str(98) + " " + str(
            math.sqrt(pow(self.x[93] - self.x[98], 2) + pow(self.y[93] - self.y[98], 2))) + "\n")
        f.write(str(94) + " " + str(95) + " " + str(
            math.sqrt(pow(self.x[94] - self.x[95], 2) + pow(self.y[94] - self.y[95], 2))) + "\n")
        f.write(str(95) + " " + str(96) + " " + str(
            math.sqrt(pow(self.x[95] - self.x[96], 2) + pow(self.y[95] - self.y[96], 2))) + "\n")
        f.write(str(96) + " " + str(97) + " " + str(
            math.sqrt(pow(self.x[96] - self.x[97], 2) + pow(self.y[96] - self.y[97], 2))) + "\n")
        f.write(str(97) + " " + str(98) + " " + str(
            math.sqrt(pow(self.x[97] - self.x[98], 2) + pow(self.y[97] - self.y[98], 2))) + "\n")
        f.write(str(97) + " " + str(106) + " " + str(
            math.sqrt(pow(self.x[97] - self.x[106], 2) + pow(self.y[97] - self.y[106], 2))) + "\n")
        f.write(str(97) + " " + str(107) + " " + str(
            math.sqrt(pow(self.x[97] - self.x[107], 2) + pow(self.y[97] - self.y[107], 2))) + "\n")
        f.write(str(98) + " " + str(99) + " " + str(
            math.sqrt(pow(self.x[98] - self.x[99], 2) + pow(self.y[98] - self.y[99], 2))) + "\n")
        f.write(str(99) + " " + str(100) + " " + str(
            math.sqrt(pow(self.x[99] - self.x[100], 2) + pow(self.y[99] - self.y[100], 2))) + "\n")
        f.write(str(99) + " " + str(103) + " " + str(
            math.sqrt(pow(self.x[99] - self.x[103], 2) + pow(self.y[99] - self.y[103], 2))) + "\n")
        f.write(str(100) + " " + str(101) + " " + str(
            math.sqrt(pow(self.x[100] - self.x[101], 2) + pow(self.y[100] - self.y[101], 2))) + "\n")
        f.write(str(101) + " " + str(102) + " " + str(
            math.sqrt(pow(self.x[101] - self.x[102], 2) + pow(self.y[101] - self.y[102], 2))) + "\n")
        f.write(str(102) + " " + str(111) + " " + str(
            math.sqrt(pow(self.x[102] - self.x[111], 2) + pow(self.y[102] - self.y[111], 2))) + "\n")
        f.write(str(103) + " " + str(104) + " " + str(
            math.sqrt(pow(self.x[103] - self.x[104], 2) + pow(self.y[103] - self.y[104], 2))) + "\n")
        f.write(str(104) + " " + str(105) + " " + str(
            math.sqrt(pow(self.x[104] - self.x[105], 2) + pow(self.y[104] - self.y[105], 2))) + "\n")
        f.write(str(105) + " " + str(106) + " " + str(
            math.sqrt(pow(self.x[105] - self.x[106], 2) + pow(self.y[105] - self.y[106], 2))) + "\n")
        f.write(str(106) + " " + str(107) + " " + str(
            math.sqrt(pow(self.x[106] - self.x[107], 2) + pow(self.y[106] - self.y[107], 2))) + "\n")
        f.write(str(106) + " " + str(111) + " " + str(
            math.sqrt(pow(self.x[106] - self.x[111], 2) + pow(self.y[106] - self.y[111], 2))) + "\n")
        f.write(str(107) + " " + str(108) + " " + str(
            math.sqrt(pow(self.x[107] - self.x[108], 2) + pow(self.y[107] - self.y[108], 2))) + "\n")
        f.write(str(108) + " " + str(109) + " " + str(
            math.sqrt(pow(self.x[108] - self.x[109], 2) + pow(self.y[108] - self.y[109], 2))) + "\n")
        f.write(str(109) + " " + str(110) + " " + str(
            math.sqrt(pow(self.x[109] - self.x[110], 2) + pow(self.y[109] - self.y[110], 2))) + "\n")
        f.write(str(110) + " " + str(111) + " " + str(
            math.sqrt(pow(self.x[110] - self.x[111], 2) + pow(self.y[110] - self.y[111], 2))) + "\n")
        f.write(str(110) + " " + str(112) + " " + str(
            math.sqrt(pow(self.x[110] - self.x[112], 2) + pow(self.y[110] - self.y[112], 2))) + "\n")


        f.close()






