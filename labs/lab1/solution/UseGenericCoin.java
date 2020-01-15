package lab1;

public class UseGenericCoin {

	public static void main(String[] args) {
		GenericCoin coin1 = new GenericCoin();
		GenericCoin coin2 = new GenericCoin();
		
		int coin1Heads = 0;
		int coin2Heads = 0;
		
		for (int i = 0; i < 100; i++) {
			coin1.toss();
			
			if (coin1.isHeads())
				++coin1Heads;
			
			coin2.toss();
			
			if (coin2.isHeads())
				++coin2Heads;
		}
		
		System.out.println("Coin 1 landed on heads " + (coin1Heads/100.0)*100 + "% of the time.");
		System.out.println("Coin 2 landed on heads " + (coin2Heads/100.0)*100 + "% of the time.");

		if (coin1Heads > coin2Heads)
			System.out.println("The first coin was heads " + (coin1Heads-coin2Heads) + " more times");
		else if (coin2Heads > coin1Heads)
			System.out.println("The first coin was heads " + (coin2Heads-coin1Heads) + " more times");	
		else
			System.out.println("Both coins had the same number of heads.");
		
	}

}
