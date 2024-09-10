#include "lists.h"

/**
 * insert_node - Function to inserts a number into a sorted singly linked list.
 * @head: pointer to pointer to the head of LL
 * @number: value to put in new node
 *
 * Return: (new_node) which is the pointer of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	if (!(*head) || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (temp->next && temp->next->n < number)
	{
		temp = temp->next;
	}
	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
