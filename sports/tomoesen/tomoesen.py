# -*- coding: utf-8 -*-

import random
import collections

PLAYERS_NUM = 3
POWER = PLAYERS_NUM * [100]
result = [] # ���ʏW�v�p�̃��X�g
REPEAT = 140000

# �ΐ�
def Battle(POWER_1, POWER_2):
    prob_win_1 = POWER_1 / (POWER_1 + POWER_2)
    prob_judge = random.random()   
    if prob_win_1 > prob_judge:
        return True
    else:
        return False

for i in range(REPEAT):
    check = True #�I������p�̕ϐ�
    # �����ݒ�
    win_count = 1
    player_1 = 0
    player_2 = 1
    last_winner = 2 #�ŏ��ɐ��Ȃ�player
    reserve_player = []    
    for j in range(2, PLAYERS_NUM):
        reserve_player.append(j)
    
    while check:
        if Battle(POWER[player_1], POWER[player_2]):
            winner = player_1
            loser = player_2
            player_2 = reserve_player[0]
        else:
            winner = player_2
            loser = player_1
            player_1 = reserve_player[0]
        reserve_player.pop(0)
        reserve_player.append(loser)
        #�I������
        if last_winner == winner:
            win_count += 1            
            if win_count == PLAYERS_NUM - 1:
                check = False
        else:
            last_winner = winner
            win_count = 1
            
    result.append(winner)

count_dict = collections.Counter(result)
for i in range(PLAYERS_NUM):
    print(str(i) + "�̏���:" + str(count_dict[i] / REPEAT))