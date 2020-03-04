import static org.junit.Assert.*;

import org.junit.Test;

public class QueensTest {

	@Test
	public void testUnderAttack() {
		Queens q = new Queens(10);
		char[][] b = q.getBoard();
		q.clearBoard();
		
		// test left diagonal
		b[0][0] = 'Q';
		assertTrue(q.isUnderAttack(9, 9));
		assertTrue(q.isUnderAttack(5,5));
		assertTrue(q.isUnderAttack(1,1));
		
		b[0][0] = '*';
		assertFalse(q.isUnderAttack(9, 9));
		assertFalse(q.isUnderAttack(5,5));
		assertFalse(q.isUnderAttack(1,1));
		
		//test right diagonal
		b[0][9] = 'Q';
		assertTrue(q.isUnderAttack(9, 0));
		assertTrue(q.isUnderAttack(4,5));
		assertTrue(q.isUnderAttack(1,8));
		
		b[0][9] = '*';
		assertFalse(q.isUnderAttack(9, 0));
		assertFalse(q.isUnderAttack(4,5));
		assertFalse(q.isUnderAttack(1,8));
		
		// test column
		b[0][9] = 'Q';
		assertTrue(q.isUnderAttack(9,9));
		
		b[0][9] = '*';
		assertFalse(q.isUnderAttack(9,9));
		
		
	}

}
