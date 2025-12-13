import { api } from './api'
import { ShoppingList } from '../types/shopping'

export async function getShoppingLists(): Promise<ShoppingList[]> {
  const response = await api.get<ShoppingList[]>('/lists/')
  return response.data
}
