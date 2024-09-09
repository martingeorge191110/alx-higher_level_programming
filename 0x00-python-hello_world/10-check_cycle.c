#include "lists.h"

/**
 * check_cycle - Function to check whether the linked list has a Cycle or not
 * @list: Single linked list
 *
 * Return: (0) if has no Cycle
 * otherwise - (1)
 */

int check_cycle(listint_t *list)
{
	listint_t *oneMove = list;
	listint_t *twoMoves = list;

	while (twoMoves && twoMoves->next)
	{
		oneMove = oneMove->next;
		twoMoves = twoMoves->next->next;

		if (oneMove == twoMoves)
			return (1);
	}

	return (0);
}
