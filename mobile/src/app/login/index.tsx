import React, { useState } from "react";
import {
  SafeAreaView,
  View,
  Text,
  TouchableOpacity,
  ActivityIndicator,
  StyleSheet,
} from "react-native";
import * as WebBrowser from "expo-web-browser";

const API_BASE_URL = "http://192.168.1.10:8000";
// Example:
// const API_BASE_URL = "http://192.168.1.10:8000";

export default function Login() {
  const [loading, setLoading] = useState(false);

  const googleLogin = async () => {
    try {
      setLoading(true);

      const redirectUrl = `${API_BASE_URL}/auth/google/login`;

      await WebBrowser.openBrowserAsync(redirectUrl);

      setLoading(false);
    } catch (error) {
      console.log("OAuth Failed:", error);
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.card}>
        <Text style={styles.title}>Welcome Back</Text>

        <Text style={styles.subtitle}>
          Sign in securely with your Google account to continue using Smart Mail
          Manager.
        </Text>

        <TouchableOpacity
          style={styles.googleButton}
          onPress={googleLogin}
          disabled={loading}
        >
          {loading ? (
            <ActivityIndicator color="#fff" />
          ) : (
            <Text style={styles.buttonText}>
              Continue with Google
            </Text>
          )}
        </TouchableOpacity>

        <Text style={styles.note}>
          Secure OAuth Authentication
        </Text>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#0F172A",
    justifyContent: "center",
    paddingHorizontal: 25,
  },

  card: {
    backgroundColor: "#1E293B",
    borderRadius: 20,
    padding: 30,
    alignItems: "center",

    shadowColor: "#000",
    shadowOpacity: 0.25,
    shadowRadius: 10,
    shadowOffset: {
      width: 0,
      height: 5,
    },

    elevation: 8,
  },

  title: {
    fontSize: 32,
    fontWeight: "bold",
    color: "#FFFFFF",
  },

  subtitle: {
    color: "#CBD5E1",
    fontSize: 16,
    textAlign: "center",
    marginTop: 15,
    lineHeight: 24,
  },

  googleButton: {
    marginTop: 35,
    backgroundColor: "#2563EB",
    width: "100%",
    paddingVertical: 16,
    borderRadius: 14,
    alignItems: "center",
  },

  buttonText: {
    color: "#FFFFFF",
    fontSize: 16,
    fontWeight: "bold",
  },

  note: {
    marginTop: 20,
    color: "#94A3B8",
    fontSize: 14,
  },
});