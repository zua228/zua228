import java.util.Stack;

public class Test {
    public static boolean isValid(String s){
        Stack<Character> stack=new Stack<>();
        if(!s.isEmpty()){
        for (char c :s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else if (stack.peek() == mapOfChar(c)) {
                stack.pop();
            }else{
                return false;
            }
        }
        }else return false;
        if (stack.isEmpty())
            return  true;
        return false;
    }
    private static char mapOfChar(char c){
        char a = 0;
        if(c ==')') {
            a= '(';
        }
        else if(c ==']') {
            a= '[';
        }
        else if(c=='}')
        {
            a= '{';
        }
        return a;
    }

    public static void main(String[] args) {
        boolean valid = isValid("{{[]}(){[()]}}");
        System.out.println(valid);
        //,[(]),{{,"",{}{}{},{[]}(){[()]}
        System.out.println();
    }
}
