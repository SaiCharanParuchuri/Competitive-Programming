arrLen =arr. arrLen;
productArray = new int[arrLen];
product = 1	;
for (int i=0; i< arrLen; i++)
{
	productArray[i] = product;
	product *= arr[i];
}

product = 1;

for (int i= arrLen-1; i>0; i--)
{
	productArray[i] *= product;
	product *= arr[i];
}
productArray[0] *= product;

return productArray;



public static int[] getProductsOfAllIntsExceptAtIndex(int[] arr) {

        // make an array of the products
        int arrLen =arr.length;
        int[] productArray = new int[arrLen];
        
        // if(arrLen==0){
        //     return productArray;
        // }
        
        if(arrLen==1){
            return productArray;
        }
        
        
        int product = 1	;
        for (int i=0; i< arrLen; i++)
        {
        	productArray[i] = product;
        	product *= arr[i];
        }
        
        product = 1;
        
        for (int i= arrLen-1; i>0; i--)
        {
        	productArray[i] *= product;
        	product *= arr[i];
        }
        productArray[0] *= product;
        
        return productArray;
    }