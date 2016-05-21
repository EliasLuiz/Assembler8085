#!/usr/bin/python

#Converte inteiro para hexadecimal de forma porca
def int2hex(num):
    hexa = list(range(10))
    hexa = [str(i) for i in hexa]
    hexa += ['A', 'B', 'C', 'D', 'E', 'F']
    res = ""
    while num / 16 > 0:
        res += hexa[int(num % 16)]
        num = int(num / 16)
    if res == "":
        return "0"
    return res[::-1]

#Converte hexadecimal para inteiro de forma porca
def hex2int(num):
    hexa = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    num = num.upper()
    res = 0
    i = 0
    while len(num) > 0:
        val = num[-1:]
        num = num[:-1]
        if val in hexa.keys():
            val = hexa[val]
        else:
            val = int(val)
        res += val * 16**i
        i+=1
    return res

################################################################################
##                            DEFINICAO DAS INSTRUCOES                        ##
################################################################################

instrucoes = [

###########################  INSTRUCOES MAIS COMUNS

    {"regex": "^HLT$", "imediato": 0, "opcode": "76"},

    {"regex": "^MOV[ \t]+A[ \t]*,[ \t]*B$", "imediato": 0, "opcode": "78"},
    {"regex": "^MOV[ \t]+A[ \t]*,[ \t]*C$", "imediato": 0, "opcode": "79"},
    {"regex": "^MOV[ \t]+A[ \t]*,[ \t]*D$", "imediato": 0, "opcode": "7A"},
    {"regex": "^MOV[ \t]+A[ \t]*,[ \t]*E$", "imediato": 0, "opcode": "7B"},
    {"regex": "^MOV[ \t]+A[ \t]*,[ \t]*H$", "imediato": 0, "opcode": "7C"},
    {"regex": "^MOV[ \t]+A[ \t]*,[ \t]*L$", "imediato": 0, "opcode": "7D"},
    {"regex": "^MOV[ \t]+A[ \t]*,[ \t]*M$", "imediato": 0, "opcode": "7E"},

    {"regex": "^MOV[ \t]+B[ \t]*,[ \t]*A$", "imediato": 0, "opcode": "47"},
    {"regex": "^MOV[ \t]+B[ \t]*,[ \t]*B$", "imediato": 0, "opcode": "40"},
    {"regex": "^MOV[ \t]+B[ \t]*,[ \t]*C$", "imediato": 0, "opcode": "41"},
    {"regex": "^MOV[ \t]+B[ \t]*,[ \t]*D$", "imediato": 0, "opcode": "42"},
    {"regex": "^MOV[ \t]+B[ \t]*,[ \t]*E$", "imediato": 0, "opcode": "43"},
    {"regex": "^MOV[ \t]+B[ \t]*,[ \t]*H$", "imediato": 0, "opcode": "44"},
    {"regex": "^MOV[ \t]+B[ \t]*,[ \t]*L$", "imediato": 0, "opcode": "45"},
    {"regex": "^MOV[ \t]+B[ \t]*,[ \t]*M$", "imediato": 0, "opcode": "46"},

    {"regex": "^MOV[ \t]+C[ \t]*,[ \t]*A$", "imediato": 0, "opcode": "4F"},
    {"regex": "^MOV[ \t]+C[ \t]*,[ \t]*B$", "imediato": 0, "opcode": "48"},
    {"regex": "^MOV[ \t]+C[ \t]*,[ \t]*C$", "imediato": 0, "opcode": "49"},
    {"regex": "^MOV[ \t]+C[ \t]*,[ \t]*D$", "imediato": 0, "opcode": "4A"},
    {"regex": "^MOV[ \t]+C[ \t]*,[ \t]*E$", "imediato": 0, "opcode": "4B"},
    {"regex": "^MOV[ \t]+C[ \t]*,[ \t]*H$", "imediato": 0, "opcode": "4C"},
    {"regex": "^MOV[ \t]+C[ \t]*,[ \t]*L$", "imediato": 0, "opcode": "4D"},
    {"regex": "^MOV[ \t]+C[ \t]*,[ \t]*M$", "imediato": 0, "opcode": "4E"},

    {"regex": "^MOV[ \t]+D[ \t]*,[ \t]*A$", "imediato": 0, "opcode": "57"},
    {"regex": "^MOV[ \t]+D[ \t]*,[ \t]*B$", "imediato": 0, "opcode": "50"},
    {"regex": "^MOV[ \t]+D[ \t]*,[ \t]*C$", "imediato": 0, "opcode": "51"},
    {"regex": "^MOV[ \t]+D[ \t]*,[ \t]*D$", "imediato": 0, "opcode": "52"},
    {"regex": "^MOV[ \t]+D[ \t]*,[ \t]*E$", "imediato": 0, "opcode": "53"},
    {"regex": "^MOV[ \t]+D[ \t]*,[ \t]*H$", "imediato": 0, "opcode": "54"},
    {"regex": "^MOV[ \t]+D[ \t]*,[ \t]*L$", "imediato": 0, "opcode": "55"},
    {"regex": "^MOV[ \t]+D[ \t]*,[ \t]*M$", "imediato": 0, "opcode": "56"},
    
    {"regex": "^MOV[ \t]+E[ \t]*,[ \t]*A$", "imediato": 0, "opcode": "5F"},
    {"regex": "^MOV[ \t]+E[ \t]*,[ \t]*B$", "imediato": 0, "opcode": "58"},
    {"regex": "^MOV[ \t]+E[ \t]*,[ \t]*C$", "imediato": 0, "opcode": "59"},
    {"regex": "^MOV[ \t]+E[ \t]*,[ \t]*D$", "imediato": 0, "opcode": "5A"},
    {"regex": "^MOV[ \t]+E[ \t]*,[ \t]*E$", "imediato": 0, "opcode": "5B"},
    {"regex": "^MOV[ \t]+E[ \t]*,[ \t]*H$", "imediato": 0, "opcode": "5C"},
    {"regex": "^MOV[ \t]+E[ \t]*,[ \t]*L$", "imediato": 0, "opcode": "5D"},
    {"regex": "^MOV[ \t]+E[ \t]*,[ \t]*M$", "imediato": 0, "opcode": "5E"},
    
    {"regex": "^MOV[ \t]+H[ \t]*,[ \t]*A$", "imediato": 0, "opcode": "67"},
    {"regex": "^MOV[ \t]+H[ \t]*,[ \t]*B$", "imediato": 0, "opcode": "60"},
    {"regex": "^MOV[ \t]+H[ \t]*,[ \t]*C$", "imediato": 0, "opcode": "61"},
    {"regex": "^MOV[ \t]+H[ \t]*,[ \t]*D$", "imediato": 0, "opcode": "62"},
    {"regex": "^MOV[ \t]+H[ \t]*,[ \t]*E$", "imediato": 0, "opcode": "63"},
    {"regex": "^MOV[ \t]+H[ \t]*,[ \t]*H$", "imediato": 0, "opcode": "64"},
    {"regex": "^MOV[ \t]+H[ \t]*,[ \t]*L$", "imediato": 0, "opcode": "65"},
    {"regex": "^MOV[ \t]+H[ \t]*,[ \t]*M$", "imediato": 0, "opcode": "66"},
    
    {"regex": "^MOV[ \t]+L[ \t]*,[ \t]*A$", "imediato": 0, "opcode": "6F"},
    {"regex": "^MOV[ \t]+L[ \t]*,[ \t]*B$", "imediato": 0, "opcode": "68"},
    {"regex": "^MOV[ \t]+L[ \t]*,[ \t]*C$", "imediato": 0, "opcode": "69"},
    {"regex": "^MOV[ \t]+L[ \t]*,[ \t]*D$", "imediato": 0, "opcode": "6A"},
    {"regex": "^MOV[ \t]+L[ \t]*,[ \t]*E$", "imediato": 0, "opcode": "6B"},
    {"regex": "^MOV[ \t]+L[ \t]*,[ \t]*H$", "imediato": 0, "opcode": "6C"},
    {"regex": "^MOV[ \t]+L[ \t]*,[ \t]*L$", "imediato": 0, "opcode": "6D"},
    {"regex": "^MOV[ \t]+L[ \t]*,[ \t]*M$", "imediato": 0, "opcode": "6E"},
    
    {"regex": "^MOV[ \t]+M[ \t]*,[ \t]*A$", "imediato": 0, "opcode": "77"},
    {"regex": "^MOV[ \t]+M[ \t]*,[ \t]*B$", "imediato": 0, "opcode": "70"},
    {"regex": "^MOV[ \t]+M[ \t]*,[ \t]*C$", "imediato": 0, "opcode": "71"},
    {"regex": "^MOV[ \t]+M[ \t]*,[ \t]*D$", "imediato": 0, "opcode": "72"},
    {"regex": "^MOV[ \t]+M[ \t]*,[ \t]*E$", "imediato": 0, "opcode": "73"},
    {"regex": "^MOV[ \t]+M[ \t]*,[ \t]*H$", "imediato": 0, "opcode": "74"},
    {"regex": "^MOV[ \t]+M[ \t]*,[ \t]*L$", "imediato": 0, "opcode": "75"},

    {"regex": "^DCR[ \t]+A$", "imediato": 0, "opcode": "3D"},
    {"regex": "^DCR[ \t]+B$", "imediato": 0, "opcode": "05"},
    {"regex": "^DCR[ \t]+C$", "imediato": 0, "opcode": "0D"},
    {"regex": "^DCR[ \t]+D$", "imediato": 0, "opcode": "15"},
    {"regex": "^DCR[ \t]+E$", "imediato": 0, "opcode": "1D"},
    {"regex": "^DCR[ \t]+H$", "imediato": 0, "opcode": "25"},
    {"regex": "^DCR[ \t]+L$", "imediato": 0, "opcode": "2D"},
    {"regex": "^DCR[ \t]+M$", "imediato": 0, "opcode": "35"},

    {"regex": "^INR[ \t]+A$", "imediato": 0, "opcode": "3C"},
    {"regex": "^INR[ \t]+B$", "imediato": 0, "opcode": "04"},
    {"regex": "^INR[ \t]+C$", "imediato": 0, "opcode": "0C"},
    {"regex": "^INR[ \t]+D$", "imediato": 0, "opcode": "14"},
    {"regex": "^INR[ \t]+E$", "imediato": 0, "opcode": "1C"},
    {"regex": "^INR[ \t]+H$", "imediato": 0, "opcode": "24"},
    {"regex": "^INR[ \t]+L$", "imediato": 0, "opcode": "2C"},
    {"regex": "^INR[ \t]+M$", "imediato": 0, "opcode": "34"},

    {"regex": "^CMP[ \t]+A$", "imediato": 0, "opcode": "BF"},
    {"regex": "^CMP[ \t]+B$", "imediato": 0, "opcode": "B8"},
    {"regex": "^CMP[ \t]+C$", "imediato": 0, "opcode": "B9"},
    {"regex": "^CMP[ \t]+D$", "imediato": 0, "opcode": "BA"},
    {"regex": "^CMP[ \t]+E$", "imediato": 0, "opcode": "BB"},
    {"regex": "^CMP[ \t]+H$", "imediato": 0, "opcode": "BC"},
    {"regex": "^CMP[ \t]+L$", "imediato": 0, "opcode": "BD"},
    {"regex": "^CMP[ \t]+M$", "imediato": 0, "opcode": "BE"},

    {"regex": "^MVI[ \t]+A[ \t]*,[ \t]*[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "3E"},
    {"regex": "^MVI[ \t]+B[ \t]*,[ \t]*[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "06"},
    {"regex": "^MVI[ \t]+C[ \t]*,[ \t]*[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "0E"},
    {"regex": "^MVI[ \t]+D[ \t]*,[ \t]*[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "16"},
    {"regex": "^MVI[ \t]+E[ \t]*,[ \t]*[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "1E"},
    {"regex": "^MVI[ \t]+L[ \t]*,[ \t]*[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "2E"},
    {"regex": "^MVI[ \t]+M[ \t]*,[ \t]*[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "36"},
    
    {"regex": "^JM[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "FA"},
    {"regex": "^JMP[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "C3"},
    {"regex": "^JNC[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "D2"},
    {"regex": "^JNZ[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "C2"},
    {"regex": "^JP[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "F2"},
    {"regex": "^JPE[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "EA"},
    {"regex": "^JPO[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "E2"},
    {"regex": "^JZ[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "CA"},

    {"regex": "^POP[ \t]+B$", "imediato": 0, "opcode": "C1"},
    {"regex": "^POP[ \t]+D$", "imediato": 0, "opcode": "D1"},
    {"regex": "^POP[ \t]+H$", "imediato": 0, "opcode": "E1"},
    {"regex": "^POP[ \t]+PSW$", "imediato": 0, "opcode": "F1"},

    {"regex": "^PUSH[ \t]+B$", "imediato": 0, "opcode": "C5"},
    {"regex": "^PUSH[ \t]+D$", "imediato": 0, "opcode": "D5"},
    {"regex": "^PUSH[ \t]+H$", "imediato": 0, "opcode": "E5"},
    {"regex": "^PUSH[ \t]+PSW$", "imediato": 0, "opcode": "F5"},
    
    {"regex": "^CALL[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "CD"},

    {"regex": "^RET$", "imediato": 0, "opcode": "C9"},

    {"regex": "^NOP$", "imediato": 0, "opcode": "00"},





###########################  INSTRUCOES DE TRANSFERENCIA DE DADOS

    {"regex": "^LDA[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "3A"},

    {"regex": "^LDAX[ \t]+B$", "imediato": 0, "opcode": "0A"},
    {"regex": "^LDAX[ \t]+D$", "imediato": 0, "opcode": "3A"},

    {"regex": "^LHLD[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 2, "opcode": "2A"},

    {"regex": "^LXI[ \t]+B[ \t]*,[ \t]*([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "01"},
    {"regex": "^LXI[ \t]+D[ \t]*,[ \t]*([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "11"},
    {"regex": "^LXI[ \t]+H[ \t]*,[ \t]*([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "21"},
    {"regex": "^LXI[ \t]+SP[ \t]*,[ \t]*([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "31"},

    {"regex": "^SHLD[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "22"},

    {"regex": "^STA[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "32"},

    {"regex": "^STAX[ \t]+M[ \t]*,[ \t]*B$", "imediato": 0, "opcode": "02"},
    {"regex": "^STAX[ \t]+M[ \t]*,[ \t]*D$", "imediato": 0, "opcode": "12"},

    {"regex": "^XCHG$", "imediato": 0, "opcode": "EB"},





###########################  INSTRUCOES ARITMETICAS

    {"regex": "^ACI[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "CE"},

    {"regex": "^ADC[ \t]+A$", "imediato": 0, "opcode": "8F"},
    {"regex": "^ADC[ \t]+B$", "imediato": 0, "opcode": "88"},
    {"regex": "^ADC[ \t]+C$", "imediato": 0, "opcode": "89"},
    {"regex": "^ADC[ \t]+D$", "imediato": 0, "opcode": "8A"},
    {"regex": "^ADC[ \t]+E$", "imediato": 0, "opcode": "8B"},
    {"regex": "^ADC[ \t]+H$", "imediato": 0, "opcode": "8C"},
    {"regex": "^ADC[ \t]+L$", "imediato": 0, "opcode": "8D"},
    {"regex": "^ADC[ \t]+M$", "imediato": 0, "opcode": "8E"},

    {"regex": "^ADD[ \t]+A$", "imediato": 0, "opcode": "87"},
    {"regex": "^ADD[ \t]+B$", "imediato": 0, "opcode": "80"},
    {"regex": "^ADD[ \t]+C$", "imediato": 0, "opcode": "81"},
    {"regex": "^ADD[ \t]+D$", "imediato": 0, "opcode": "82"},
    {"regex": "^ADD[ \t]+E$", "imediato": 0, "opcode": "83"},
    {"regex": "^ADD[ \t]+H$", "imediato": 0, "opcode": "84"},
    {"regex": "^ADD[ \t]+L$", "imediato": 0, "opcode": "85"},
    {"regex": "^ADD[ \t]+M$", "imediato": 0, "opcode": "86"},

    {"regex": "^ADI[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "C6"},

    {"regex": "^DAA$", "imediato": 0, "opcode": "27"},

    {"regex": "^DAD[ \t]+B$", "imediato": 0, "opcode": "09"},
    {"regex": "^DAD[ \t]+D$", "imediato": 0, "opcode": "19"},
    {"regex": "^DAD[ \t]+H$", "imediato": 0, "opcode": "29"},
    {"regex": "^DAD[ \t]+SP$", "imediato": 0, "opcode": "39"},

    {"regex": "^DCX[ \t]+B$", "imediato": 0, "opcode": "0B"},
    {"regex": "^DCX[ \t]+D$", "imediato": 0, "opcode": "1B"},
    {"regex": "^DCX[ \t]+H$", "imediato": 0, "opcode": "2B"},
    {"regex": "^DCX[ \t]+SP$", "imediato": 0, "opcode": "3B"},

    {"regex": "^INX[ \t]+B$", "imediato": 0, "opcode": "03"},
    {"regex": "^INX[ \t]+D$", "imediato": 0, "opcode": "13"},
    {"regex": "^INX[ \t]+H$", "imediato": 0, "opcode": "23"},
    {"regex": "^INX[ \t]+SP$", "imediato": 0, "opcode": "33"},

    {"regex": "^SBB[ \t]+A$", "imediato": 0, "opcode": "9F"},
    {"regex": "^SBB[ \t]+B$", "imediato": 0, "opcode": "98"},
    {"regex": "^SBB[ \t]+C$", "imediato": 0, "opcode": "99"},
    {"regex": "^SBB[ \t]+D$", "imediato": 0, "opcode": "9A"},
    {"regex": "^SBB[ \t]+E$", "imediato": 0, "opcode": "9B"},
    {"regex": "^SBB[ \t]+H$", "imediato": 0, "opcode": "9C"},
    {"regex": "^SBB[ \t]+L$", "imediato": 0, "opcode": "9D"},
    {"regex": "^SBB[ \t]+M$", "imediato": 0, "opcode": "9E"},

    {"regex": "^SBI[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "DE"},

    {"regex": "^SUB[ \t]+A$", "imediato": 0, "opcode": "97"},
    {"regex": "^SUB[ \t]+B$", "imediato": 0, "opcode": "90"},
    {"regex": "^SUB[ \t]+C$", "imediato": 0, "opcode": "91"},
    {"regex": "^SUB[ \t]+D$", "imediato": 0, "opcode": "92"},
    {"regex": "^SUB[ \t]+E$", "imediato": 0, "opcode": "93"},
    {"regex": "^SUB[ \t]+H$", "imediato": 0, "opcode": "94"},
    {"regex": "^SUB[ \t]+L$", "imediato": 0, "opcode": "95"},
    {"regex": "^SUB[ \t]+M$", "imediato": 0, "opcode": "96"},

    {"regex": "^SUI[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "D6"},





###########################  INSTRUCOES LOGICAS

    {"regex": "^ANA[ \t]+A$", "imediato": 0, "opcode": "A7"},
    {"regex": "^ANA[ \t]+B$", "imediato": 0, "opcode": "A0"},
    {"regex": "^ANA[ \t]+C$", "imediato": 0, "opcode": "A1"},
    {"regex": "^ANA[ \t]+D$", "imediato": 0, "opcode": "A2"},
    {"regex": "^ANA[ \t]+E$", "imediato": 0, "opcode": "A3"},
    {"regex": "^ANA[ \t]+H$", "imediato": 0, "opcode": "A4"},
    {"regex": "^ANA[ \t]+L$", "imediato": 0, "opcode": "A5"},
    {"regex": "^ANA[ \t]+M$", "imediato": 0, "opcode": "A6"},

    {"regex": "^ANI[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "E6"},

    {"regex": "^CMC$", "imediato": 0, "opcode": "3F"},

    {"regex": "^ORA[ \t]+A$", "imediato": 0, "opcode": "B7"},
    {"regex": "^ORA[ \t]+B$", "imediato": 0, "opcode": "B0"},
    {"regex": "^ORA[ \t]+C$", "imediato": 0, "opcode": "B1"},
    {"regex": "^ORA[ \t]+D$", "imediato": 0, "opcode": "B2"},
    {"regex": "^ORA[ \t]+E$", "imediato": 0, "opcode": "B3"},
    {"regex": "^ORA[ \t]+H$", "imediato": 0, "opcode": "B4"},
    {"regex": "^ORA[ \t]+L$", "imediato": 0, "opcode": "B5"},
    {"regex": "^ORA[ \t]+M$", "imediato": 0, "opcode": "B6"},

    {"regex": "^ORI[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "F6"},

    {"regex": "^RAL$", "imediato": 0, "opcode": "17"},

    {"regex": "^RAR$", "imediato": 0, "opcode": "1F"},

    {"regex": "^RC$", "imediato": 0, "opcode": "D8"},

    {"regex": "^RLC$", "imediato": 0, "opcode": "07"},

    {"regex": "^RNC$", "imediato": 0, "opcode": "D0"},

    {"regex": "^RRC$", "imediato": 0, "opcode": "0F"},

    {"regex": "^XRA[ \t]+A$", "imediato": 0, "opcode": "AF"},
    {"regex": "^XRA[ \t]+B$", "imediato": 0, "opcode": "A8"},
    {"regex": "^XRA[ \t]+C$", "imediato": 0, "opcode": "A9"},
    {"regex": "^XRA[ \t]+D$", "imediato": 0, "opcode": "AA"},
    {"regex": "^XRA[ \t]+E$", "imediato": 0, "opcode": "AB"},
    {"regex": "^XRA[ \t]+H$", "imediato": 0, "opcode": "AC"},
    {"regex": "^XRA[ \t]+L$", "imediato": 0, "opcode": "AD"},
    {"regex": "^XRA[ \t]+M$", "imediato": 0, "opcode": "AE"},






###########################  INSTRUCOES DE CONTROLE, PILHA E IO

    {"regex": "^CC[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "DC"},
    
    {"regex": "^CM[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "FC"},

    {"regex": "^CMA$", "imediato": 0, "opcode": "2F"},

    {"regex": "^CMC$", "imediato": 0, "opcode": "3F"},
    
    {"regex": "^CNC[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "D4"},

    {"regex": "^CNZ[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "C4"},
    
    {"regex": "^CP[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "F4"},
    
    {"regex": "^CPE[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "EC"},
    
    {"regex": "^CPI[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "FE"},
    
    {"regex": "^CPO[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "E4"},
    
    {"regex": "^CZ[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "CC"},

    {"regex": "^DI$", "imediato": 0, "opcode": "F3"},

    {"regex": "^EI$", "imediato": 0, "opcode": "FB"},
    
    {"regex": "^IN[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "DB"},
    
    {"regex": "^JC[ \t]+([0-9ABCDEF]{1,8}|[^0-9][^ \t\,]*)$", "imediato": 2, "opcode": "DA"},
    
    {"regex": "^ORI[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "F6"},
    
    {"regex": "^OUT[ \t]+[0-9ABCDEF]{1,4}$", "imediato": 1, "opcode": "D3"},

    {"regex": "^PCHL$", "imediato": 0, "opcode": "E9"},

    {"regex": "^RC$", "imediato": 0, "opcode": "D8"},

    {"regex": "^RIM$", "imediato": 0, "opcode": "20"},

    {"regex": "^RM$", "imediato": 0, "opcode": "F8"},

    {"regex": "^RNC$", "imediato": 0, "opcode": "D0"},

    {"regex": "^RNZ$", "imediato": 0, "opcode": "C0"},

    {"regex": "^RP$", "imediato": 0, "opcode": "F0"},

    {"regex": "^RPE$", "imediato": 0, "opcode": "E8"},

    {"regex": "^RPO$", "imediato": 0, "opcode": "E0"},

    {"regex": "^RST[ \t]+0$", "imediato": 0, "opcode": "C7"},
    {"regex": "^RST[ \t]+1$", "imediato": 0, "opcode": "CF"},
    {"regex": "^RST[ \t]+2$", "imediato": 0, "opcode": "D7"},
    {"regex": "^RST[ \t]+3$", "imediato": 0, "opcode": "CF"},
    {"regex": "^RST[ \t]+4$", "imediato": 0, "opcode": "E7"},
    {"regex": "^RST[ \t]+5$", "imediato": 0, "opcode": "EF"},
    {"regex": "^RST[ \t]+6$", "imediato": 0, "opcode": "F7"},
    {"regex": "^RST[ \t]+7$", "imediato": 0, "opcode": "FF"},

    {"regex": "^RZ$", "imediato": 0, "opcode": "C8"},

    {"regex": "^SIM$", "imediato": 0, "opcode": "30"},

    {"regex": "^SPHL$", "imediato": 0, "opcode": "F9"},

    {"regex": "^STC$", "imediato": 0, "opcode": "37"},

    {"regex": "^XRI$", "imediato": 0, "opcode": "EE"},

    {"regex": "^XTHL$", "imediato": 0, "opcode": "E3"},
]







################################################################################
##                       LEITURA DO ARQUIVO E MONTAGEM                        ##
################################################################################

#Definindo argumentos da linha de comando
import argparse
parser = argparse.ArgumentParser(description="Montador para assembly do processador Intel 8085.\n\nNotas:\n  1) Labels nao devem conter os caracteres ' ' e ',' e devem estar seguidos de ':'.\n  2) Labels devem estar em linha separada de instrucao.\n  3) Labels sao case-sensitive, enquanto instrucoes sao case-insensitive.\n  4) Todos os numeros informados sao tratados como hexadecimal.")
parser.add_argument("input", metavar="ArquivoFonte", help="Arquivo contendo o codigo-fonte em assembly.")
parser.add_argument("output", metavar="ArquivoFinal", help="Arquivo no qual sera escrito o resultado hexadecimal.")
parser.add_argument("-a", "--abacus", help="Arquivo final sera gerado no formato interpretado pelo programa Abacus.", action="store_true", default=False)
parser.add_argument("-e", "--endereco", metavar="Endereco", help="Endereco da posicao de memoria da primeira instrucao do programa. Desnecessario caso o parametro -a ou --abacus seja passado.", default=0)

#Lendo argumentos da linha de comando
args = parser.parse_args()

#Lendo arquivo, retirando comentarios, linhas em branco e espacos no inicio e final
fonte = []
contLinha = 1
with open(args.input, "r") as arquivo:
    for linha in arquivo:
        #Remocao de comentarios
        linha = linha[:(linha.find('#') if linha.find('#') != -1 else None)]
        #Remocao de linhas em branco
        if linha and linha != "\n":
            linha = linha.strip()
            fonte.append( (contLinha, linha, linha.endswith(':')) )
        contLinha+=1

#Parsing codigo fonte lido
import re
hexadecimalParcial = []
for nLinha, linha, isLabel in fonte:
    valida = False
    #Se e um label
    if isLabel:
        hexadecimalParcial.append( (linha.strip(':').strip(), nLinha, 2, True) )
        continue
    for instrucao in instrucoes:
        #Se e uma instrucao reconhecida
        if re.match(instrucao["regex"], linha, re.I):
            valida = True
            #Armazena opcode da instrucao
            hexa = instrucao["opcode"] + " "
            #Se instrucao possui imediato
            if instrucao["imediato"] > 0:
                res = re.search("[\t \,]+[0-9ABCDEF]+$", linha, re.I)
                #Instrucao com label - armazena label
                if not res:
                    hexa += re.split("[ \t\,]", linha)[-1]
                #Instrucao com imediato - armazena imediato
                else:
                    hexa += res.group(0).lstrip('0').upper()
            hexadecimalParcial.append( (hexa, nLinha, instrucao["imediato"], False) )
            break
    #Se nao e uma instrucao reconhecida
    if not valida:
        raise Exception("Instrucao invalida na linha %s: %s" % (nLinha, linha))

#Convertendo labels e imediatos para formato
if args.abacus:
    programCounter = 8192
else:
    programCounter = int(args.endereco)
#Dicionario para armazenar os enderecos dos labels
labels = {}
#Lista para armazenar o hexadecimal do programa
hexadecimalFinal = []
#Parsing o pseudo codigo pegando o endereco dos labels
for hexa, _, tamImediato, isLabel in hexadecimalParcial:
    if isLabel:
        labels[hexa] = int2hex(programCounter)
    else:
        programCounter += 1 + tamImediato
#Retirando labels da lista
hexadecimalParcial = [i for i in hexadecimalParcial if not i[3]]


#Parsing o pseudo codigo colocando os labels e imediatos no formato
for hexa, nLinha, tamImediato, isLabel in hexadecimalParcial:        
    if len(hexa.strip()) == 2:
        hexadecimalFinal.append(hexa.strip())
        programCounter += 1
    else:
        imediato = re.split("[ \,]", hexa)[-1]
        #Caso imediato seja label
        if imediato in labels.keys():
            imediato = labels[imediato]
        #Caso nao seja hexadecimal
        elif imediato and not re.search("^[0-9ABCDEF]+$", imediato, re.I):
            raise Exception("Imediato invalido na linha %s: %s" % (nLinha, imediato))
        #Imediato maior que aceito pela instrucao
        if len(imediato) > 2 * tamImediato:
            raise Exception("Imediato maior que suportado na linha %s: %s" % (nLinha, imediato))
        #Adicionando 0's a esquerda para completar os bits
        while len(imediato) < 2 * tamImediato:
            imediato = "0" + imediato
        #Convertendo imediato para little endian
        hexa = hexa.split(" ")[0] + " " + imediato[2:] + " " + imediato[:2] if len(imediato) > 2 else hexa.split(" ")[0] + " " + imediato[:2]
        hexadecimalFinal.append(hexa)
        #Incrementando o contador de programa
        programCounter += int( len( hexadecimalFinal[-1].replace(" ", "") ) / 2 )





################################################################################
##                       ESCRITA NO ARQUIVO DE SAIDA                          ##
################################################################################

#Escrita do resultado em arquivo
with open(args.output, "w") as arquivo:
    #Escrita em arquivo no formato do abacus
    if args.abacus:
        listaHexa = []
        for i in hexadecimalFinal:
            listaHexa += i.split(" ")
        while len(listaHexa) % 16 != 0:
            listaHexa += ["00"]
        nLinhas = int(len(listaHexa) / 16)

        prefixo = 66048
        contLinha = 0

        for i in range(nLinhas):
            hexa = listaHexa[16*contLinha:16*(contLinha+1)]
            
            checksum = 208
            for i in hexa:
                checksum -= hex2int(i)
                checksum = checksum if checksum >= 0 else checksum + 256
            checksum -= 16 * contLinha
            checksum = checksum if checksum >= 0 else checksum + 256
            checksum = int2hex(checksum)
            checksum = checksum if len(checksum) == 2 else "0" + checksum

            linha = ":"
            linha += int2hex(prefixo+contLinha) + "000"
            linha += "".join(hexa)
            linha += checksum + "\n"

            arquivo.write(linha)

            contLinha += 1

        arquivo.write(":00000001FF")
    #Escrita da string hexadecimal separada por espaco
    else:
        arquivo.write(" ".join(hexadecimalFinal))
