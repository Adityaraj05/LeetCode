class Solution {
    public String intToRoman(int num) {
        int [] values ={ 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
        String [] roman = {"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
        StringBuilder sb = new StringBuilder();
        for(int i=values.length-1; i >=0 && num>0; i--){
            while(num >= values[i]){   // for exmaple num = 5 ; if 5 >= 1000 no then i-- , till 5>=5 yes then subtract 5 - 5 = 0 then terminate the loop and append "V" in  string builder 
                num -= values[i];
                sb.append(roman[i]);

            }
        }
        return sb.toString();
    }
}
