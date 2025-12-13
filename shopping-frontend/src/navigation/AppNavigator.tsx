import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import { ShoppingListsScreen } from "../screens/ShoppingListsScreen";
//import { ShoppingListItemsScreen } from "../screens/ShoppingListItemsScreen";

export type RootStackParamList = {
  Lists: undefined;
  Items: { listId: number; title: string };
};

const Stack = createNativeStackNavigator<RootStackParamList>();

export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Lists"
          component={ShoppingListsScreen}
          options={{ title: "Minhas Listas" }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
