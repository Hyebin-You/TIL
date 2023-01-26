import React from "react";
import { Unity, useUnityContext } from "react-unity-webgl";

const UnityGame = () => {
  const { unityProvider } = useUnityContext({
    loaderUrl: "unitybuild/build.loader.js",
    dataUrl: "unitybuild/build.data",
    frameworkUrl: "unitybuild/build.framework.js",
    codeUrl: "unitybuild/build.wasm",

    symbolsUrl: "unitybuild/build.symbols.json",
    streamingAssetsUrl: "StreamingAssets",
    companyName: "DefaultCompany",
    productName: "3D_test",
    productVersion: "0.1",
  });

  const myInstance = unityProvider;

  return (
    <div>
      <Unity
        unityProvider={unityProvider}
        style={{ width: 900, height: 600 }}
      />
    </div>
  );
};

export default UnityGame;
