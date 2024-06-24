import React, { useState } from "react";
import {
  Button,
  TextInput,
  Tab,
  TabGroup,
  TabList,
  TabPanel,
  TabPanels,
} from "@tremor/react";
export default function FRR() {
  const [cmd, setCmd] = useState("");


  const handleSubmit = () => {
    console.log(cmd)
  }
  return (
    <div className="h-screen">
      <div className="font-medium text-[20px] mt-4">FRR Page</div>
      <div className="my-6">
        <TabGroup defaultIndex={1}>
          <TabList variant="line">
            <Tab value="1">System</Tab>
            <Tab value="2">BGP</Tab>
            <Tab value="3">OSPF</Tab>
            <Tab value="4">Filtering</Tab>
            <Tab value="5">Routemap</Tab>
          </TabList>
          <TabPanels>
            <TabPanel>
              <div class="my-4">
                <label class="block text-gray-700 text-sm mb-2" for="username">
                  Input the command
                </label>
                <div className="flex gap-4 my-4">
                  <TextInput
                    id="command"
                    type="text"
                    className="w-fit"
                    value={cmd}
                    onChange={(event)=>{setCmd(event.target.value)}}
                    placeholder="show interfaces"
                  />
                  <Button onClick={handleSubmit} className="px-4 py-2 font-medium text-[14px]   rounded-md ">
                    Execute
                  </Button>
                </div>
                <div className="font-medium mt-4">Output</div>
              </div>
            </TabPanel>
            <TabPanel>BGP Tab</TabPanel>
            <TabPanel>OSPF Tab</TabPanel>
            <TabPanel>Filtering Tab</TabPanel>
            <TabPanel>Routemap Tab</TabPanel>
          </TabPanels>
        </TabGroup>
      </div>
    </div>
  );
}
