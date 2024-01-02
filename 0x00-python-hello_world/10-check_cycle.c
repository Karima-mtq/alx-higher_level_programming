#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *lent, *rapid;

	if (list == NULL || list->next == NULL)
		return (0);

	lent = list->next;
	rapid = list->next->next;

	while (lent && rapid && rapid->next)
	{
		if (lent == rapid)
			return (1);

		lent = lent->next;
		rapid = rapid->next->next;
	}

	return (0);
}
