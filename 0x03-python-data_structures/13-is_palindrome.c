#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - Function to Check whether the list is palindrome
 * @head: pointer to the the head of the list
 *
 * Return: (0) Succes
 * otherwiese - (1)
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int list[2000], index = 0, counter = 0;

	if (!(*head))
		return (1);

	while (temp)
	{
		list[counter] = temp->n;
		temp = temp->next;
		counter++;
	}

	for (index = 0; index < counter; index++)
	{
		if (list[index] != list[counter - (index + 1)])
			return (0);
	}

	return (1);
}
