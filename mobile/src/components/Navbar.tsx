import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";
import { router } from "expo-router";
import Login from "@/app/login";

export default function Navbar() {
  return (
    <View style={styles.navbar}>
      <Text style={styles.logo}>mailM</Text>

      <TouchableOpacity
        style={styles.loginBtn}
        onPress={() => router.push("/login/index")}
      >
        <Text style={styles.loginText}>Login</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  navbar: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    paddingHorizontal: 20,
    paddingTop: 20,
    paddingBottom: 10,
  },

  logo: {
    color: "#fff",
    fontSize: 28,
    fontWeight: "bold",
  },

  loginBtn: {
    backgroundColor: "#fff",
    paddingHorizontal: 18,
    paddingVertical: 10,
    borderRadius: 10,
  },

  loginText: {
    color: "#1E3A8A",
    fontWeight: "bold",
  },
});