import { useEffect, useState } from "react";
import {
  View,
  Text,
  FlatList,
  Switch,
  StyleSheet,
} from "react-native";
import { NativeStackScreenProps } from "@react-navigation/native-stack";

import { RootStackParamList } from "../navigation/AppNavigator";
import { Item } from "../types/shopping";
import { getItems, toggleItem } from "../services/api";

type Props = NativeStackScreenProps<RootStackParamList, "Items">;

export default function ShoppingListItemsScreen({ route }: Props) {
  const { listId } = route.params;
  const [items, setItems] = useState<Item[]>([]);

  const loadItems = async () => {
    const data = await getItems(listId);
    setItems(data);
  };

  const handleToggle = async (item: Item) => {
    await toggleItem(item.id, !item.checked);
    loadItems();
  };

  useEffect(() => {
    loadItems();
  }, []);

  return (
    <View style={styles.container}>
      <FlatList
        data={items}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.row}>
            <Text
              style={[
                styles.name,
                item.checked && styles.checked,
              ]}
            >
              {item.name} ({item.quantity})
            </Text>
            <Switch
              value={item.checked}
              onValueChange={() => handleToggle(item)}
            />
          </View>
        )}
      />
    </View>
  );
}
