class Solution {
public:
    int reverse(int x) {
        
        int reversedno = 0, remainder;
        while(x!=0)
        {
            remainder = x%10;
            reversedno = reversedno*10+remainder;
            x/=10;
        }
        return reversedno;
    
    }
};



/*

declare reversednumber = and remainder
while(x!=0)
{
remainder = x%10,  remainder = x/10
reversedno = 0*10+remainder
x = x/10
}

Essentially we need to 
*/
