import React from "react";
import {
  SafeAreaView,
  View,
  Text,
  ScrollView,
  TouchableOpacity,
  StyleSheet,
} from "react-native";
import { router } from "expo-router";

import Navbar from "../components/Navbar";
 

export default function HomeScreen() {
  return (
    <SafeAreaView style={styles.container}>
      <Navbar />

      <ScrollView contentContainerStyle={styles.content}>
        <Text style={styles.title}>
          Smart Mail Manager
        </Text>

        <Text style={styles.subtitle}>
          Organize, filter, summarize, and manage your emails efficiently with
          AI-powered automation. Connect Gmail securely and take control of your
          inbox like never before.
        </Text>

        <View style={styles.featureContainer}>
          <Text style={styles.feature}>
            📩 Fetch Sent & Received Mails
          </Text>

          <Text style={styles.feature}>
            🔍 Filter by Sender & Date
          </Text>

          <Text style={styles.feature}>
            🤖 AI Email Summaries
          </Text>

          <Text style={styles.feature}>
            📊 Mail Dashboard Analytics
          </Text>
        </View>

        <View style={styles.buttonContainer}>
          <TouchableOpacity
            style={styles.primaryButton}
            onPress={() => router.push("/")}
          >
            <Text style={styles.primaryText}>Get Started</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.secondaryButton}
            onPress={() => router.push("/login/index")}
          >
            <Text style={styles.secondaryText}>
              View Dashboard
            </Text>
          </TouchableOpacity>
        </View>

        <View style={styles.statsContainer}>
          <View style={styles.statBox}>
            <Text style={styles.statNumber}>20+</Text>
            <Text style={styles.statLabel}>Emails Per Fetch</Text>
          </View>

          <View style={styles.statBox}>
            <Text style={styles.statNumber}>100%</Text>
            <Text style={styles.statLabel}>Secure OAuth Login</Text>
          </View>

          <View style={styles.statBox}>
            <Text style={styles.statNumber}>AI</Text>
            <Text style={styles.statLabel}>Smart Summaries</Text>
          </View>

          <View style={styles.statBox}>
            <Text style={styles.statNumber}>24/7</Text>
            <Text style={styles.statLabel}>Mail Access</Text>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#1E3A8A",
  },

  content: {
    alignItems: "center",
    paddingHorizontal: 25,
    paddingBottom: 50,
  },

  title: {
    fontSize: 40,
    fontWeight: "bold",
    color: "#fff",
    textAlign: "center",
    marginTop: 50,
  },

  subtitle: {
    color: "#DCE7FF",
    textAlign: "center",
    fontSize: 17,
    marginTop: 20,
    lineHeight: 28,
  },

  featureContainer: {
    marginTop: 35,
    width: "100%",
  },

  feature: {
    backgroundColor: "rgba(255,255,255,0.15)",
    color: "#fff",
    padding: 15,
    borderRadius: 30,
    marginBottom: 15,
    textAlign: "center",
    overflow: "hidden",
  },

  buttonContainer: {
    flexDirection: "row",
    marginTop: 35,
    gap: 15,
  },

  primaryButton: {
    backgroundColor: "#fff",
    paddingHorizontal: 22,
    paddingVertical: 14,
    borderRadius: 12,
  },

  primaryText: {
    color: "#1E3A8A",
    fontWeight: "bold",
  },

  secondaryButton: {
    borderWidth: 1,
    borderColor: "#fff",
    paddingHorizontal: 22,
    paddingVertical: 14,
    borderRadius: 12,
  },

  secondaryText: {
    color: "#fff",
    fontWeight: "bold",
  },

  statsContainer: {
    marginTop: 55,
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "center",
  },

  statBox: {
    width: 150,
    alignItems: "center",
    marginBottom: 30,
  },

  statNumber: {
    color: "#fff",
    fontSize: 30,
    fontWeight: "bold",
  },

  statLabel: {
    color: "#DCE7FF",
    textAlign: "center",
    marginTop: 5,
  },
});