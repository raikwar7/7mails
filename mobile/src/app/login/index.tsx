import React, { useState } from "react";
import {
  SafeAreaView,
  View,
  Text,
  TouchableOpacity,
  ActivityIndicator,
  StyleSheet,
  Platform,
} from "react-native";
import * as WebBrowser from "expo-web-browser";

const API_BASE_URL = "http://192.168.1.45:8000";

export default function Login() {
  const [loading, setLoading] = useState(false);

  const googleLogin = async () => {
    try {
      setLoading(true);

      // Detect platform automatically
      const platform = Platform.OS === "ios" ? "ios" : "android";

      const loginUrl = `${API_BASE_URL}/auth/google/login?platform=${platform}`;

      console.log("Opening:", loginUrl);

      await WebBrowser.openBrowserAsync(loginUrl);
    } catch (err) {
      console.log("Google Login Error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.card}>
        <Text style={styles.title}>
          Smart Mail Manager
        </Text>

        <Text style={styles.subtitle}>
          Login with your Google account.
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
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#0F172A",
    justifyContent: "center",
    padding: 20,
  },

  card: {
    backgroundColor: "#1E293B",
    borderRadius: 15,
    padding: 25,
  },

  title: {
    color: "white",
    fontSize: 28,
    fontWeight: "bold",
    textAlign: "center",
  },

  subtitle: {
    color: "#CBD5E1",
    textAlign: "center",
    marginTop: 10,
    marginBottom: 25,
  },

  googleButton: {
    backgroundColor: "#2563EB",
    padding: 16,
    borderRadius: 10,
  },

  buttonText: {
    color: "white",
    textAlign: "center",
    fontWeight: "bold",
    fontSize: 16,
  },
});