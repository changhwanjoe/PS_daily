import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;
 
public class Solution {
 
    private static int[] input,sortedInput;
    private static String str;
    private static int caseNum,changeNum,max,index,lastIndex,size,changeIndex;
    private static boolean flag,chk;
 
    public static void main(String args[]) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
 
        caseNum=Integer.parseInt(st.nextToken());
        for(int i=1;i<=caseNum;i++){
            st=new StringTokenizer(br.readLine());
            str=st.nextToken();
            input=new int[str.length()];
            sortedInput=new int[str.length()];
 
            changeNum=Integer.parseInt(st.nextToken());
            for(int j=0;j<str.length();j++){
                input[j]=str.charAt(j)-48;
            }
            sortedInput=input.clone();
            Arrays.sort(sortedInput);
 
            index=0;
            lastIndex=str.length()-1;
            size=str.length();
            max=sortedInput[str.length()-1];
            flag=true;
            chk=false;
 
 
            while(changeNum!=0){
                for(int j=0;j<size;j++){
                    if(input[j]!=sortedInput[size-1-j]){
                        flag=false;
                        break;
                    }
                }
                for(int j=size-1;j>0;j--){
                    if(sortedInput[j]==sortedInput[j-1]){
                        chk=true;
                        break;
                    }
                }
                if(chk&&flag){
                    break;
                }
                if(str.length()==2||(changeNum%2==0&&flag)){
                    change(0,1);
                    break;
                }
                else{
                    if(index<size) {
                        if (input[index] != sortedInput[size - 1 - index]) {
                            for (int j = size - 1; j > index; j--) {
                                if (input[j] == sortedInput[size - 1 - index]) {
                                    changeIndex = j;
                                    change(index, changeIndex);
                                    if (index > 0 && index < size && input[index - 1] == input[index]) {
                                        if (input[changeIndex] < input[changeIndex + 1]) {
                                            change(changeIndex, changeIndex + 1);
                                        }
                                    }
                                    break;
                                }
                            }
 
                            index++;
                            changeNum--;
                        } else if (input[index] == sortedInput[size - 1 - index]) {
                            index++;
                        }
                    }
                    else{
                        change(size - 2, size - 1);
                        changeNum--;
                    }
                }
 
 
 
            }
            System.out.print("#"+i+" ");
            for(int j=0;j<str.length();j++){
                System.out.print(input[j]);
            }
            System.out.println();
 
 
 
 
        }
 
    }
    private static void change(int i,int j){
        int tmp=input[i];
        input[i]=input[j];
        input[j]=tmp;
    }
 
}
