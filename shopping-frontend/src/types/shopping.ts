export interface ShoppingList {
  id: number
  title: string
  createdAt: string
  itemsCount: number
}

export interface Item {
  id: number;
  name: string;
  quantity: number;
  checked: boolean;
}