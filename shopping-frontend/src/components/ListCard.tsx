// src/components/ListCard.tsx
import React from "react";
import { TouchableOpacity, View, Text } from "react-native";
import styled from "styled-components/native";
import { ShoppingList } from "../types/shopping";

const Card = styled.TouchableOpacity`
  background-color: white;
  padding: 16px;
  margin-vertical: 8px;
  margin-horizontal: 16px;
  border-radius: 8px;
  elevation: 2;
`;

const Title = styled.Text`
  font-size: 16px;
  font-weight: 600;
`;

const Meta = styled.Text`
  font-size: 12px;
  color: #666;
  margin-top: 6px;
`;

type Props = {
  list: ShoppingList;
  onPress?: () => void;
};

export default function ListCard({ list, onPress }: Props) {
  return (
    <Card onPress={onPress}>
      <Title>{list.title}</Title>
      <Meta>{list.itemsCount ?? 0} itens • {list.createdAt ? new Date(list.createdAt).toLocaleDateString() : "—"}</Meta>
    </Card>
  );
}
