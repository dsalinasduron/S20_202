/**
 * 
 */
package lab1;

/**
 * @author greg
 *
 */
public class GenericCoin {
	public enum CoinSide {HEADS, TAILS};
	
	private CoinSide side;
	
	public GenericCoin() {
		side = CoinSide.HEADS;
	}
	
	public void setToHeads() {
		side = CoinSide.HEADS;
	}
	
	public void setToTails() {
		side = CoinSide.TAILS;
	}
	
	public void toss() {
		if (java.lang.Math.random() < 0.5)
			side = CoinSide.HEADS;
		else
			side = CoinSide.TAILS;
	}
	
	public boolean isHeads() {
		if (side == CoinSide.HEADS)
			return true;
		else
			return false;
	}
	
	public boolean isTails() {
		if (side == CoinSide.TAILS)
			return true;
		else
			return false;
	}
	
	public String toString() {
		if (isHeads())
			return "Heads";
		else
			return "Tails";
	}
}
