// src/components/Fab.tsx
import React from "react";
import { TouchableOpacity, Text } from "react-native";
import styled from "styled-components/native";
import { MaterialIcons } from "@expo/vector-icons";

const Button = styled.TouchableOpacity`
  position: absolute;
  right: 20px;
  bottom: 30px;
  background-color: #007bff;
  width: 56px;
  height: 56px;
  border-radius: 28px;
  align-items: center;
  justify-content: center;
  elevation: 4;
`;

export default function Fab({ onPress }: { onPress?: () => void }) {
  return (
    <Button onPress={onPress} accessibilityLabel="Adicionar lista">
      <MaterialIcons name="add" size={28} color="#fff" />
    </Button>
  );
}
