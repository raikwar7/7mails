import { useEffect } from "react";
import { ActivityIndicator, View } from "react-native";
import { router, useLocalSearchParams } from "expo-router";
import AsyncStorage from "@react-native-async-storage/async-storage";

export default function LoginSuccess() {

  const params = useLocalSearchParams();

  useEffect(() => {

    async function saveToken() {

      const token =
        typeof params.token === "string"
          ? params.token
          : undefined;

      if (!token) {

        router.replace("/");

        return;
      }

      await AsyncStorage.setItem("token", token);

      router.replace("/admin/adminDashboard");
    }

    saveToken();

  }, []);

  return (
    <View
      style={{
        flex:1,
        justifyContent:"center",
        alignItems:"center",
      }}
    >
      <ActivityIndicator size="large"/>
    </View>
  );

}