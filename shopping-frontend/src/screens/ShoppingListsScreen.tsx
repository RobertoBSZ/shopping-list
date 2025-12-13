import { useEffect, useState } from 'react'
import {
  View,
  Text,
  FlatList,
  ActivityIndicator,
  TouchableOpacity,
} from 'react-native'

import { getShoppingLists } from '../services/shoppingListsService'
import { ShoppingList } from '../types/shopping'

export function ShoppingListsScreen() {
  const [lists, setLists] = useState<ShoppingList[]>([])
  const [loading, setLoading] = useState(true)

  async function loadLists() {
    try {
      setLoading(true)
      const data = await getShoppingLists()
      setLists(data)
    } catch (error) {
      console.error('Erro ao buscar listas', error)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
  loadLists()
}, [])

  if (loading) {
    return (
      <View style={{ flex: 1, justifyContent: 'center' }}>
        <ActivityIndicator size="large" />
      </View>
    )
  }

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 24, fontWeight: 'bold', marginBottom: 16 }}>
        Minhas Listas
      </Text>

      <FlatList
        data={lists}
        keyExtractor={(item) => String(item.id)}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={{
              padding: 16,
              borderRadius: 8,
              backgroundColor: '#f2f2f2',
              marginBottom: 12,
            }}
          >
            <Text style={{ fontSize: 18, fontWeight: '600' }}>
              {item.title}
            </Text>

            <Text style={{ color: '#666' }}>
              {item.itemsCount} itens
            </Text>
          </TouchableOpacity>
        )}
      />

      {/* Botão adicionar */}
      <TouchableOpacity
        style={{
          position: 'absolute',
          right: 20,
          bottom: 20,
          width: 56,
          height: 56,
          borderRadius: 28,
          backgroundColor: '#4CAF50',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Text style={{ color: '#fff', fontSize: 28 }}>+</Text>
      </TouchableOpacity>
    </View>
  )
}
