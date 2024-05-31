import { Spacecraft } from '@src/types/spacecraft';
import React, { useEffect, useState } from 'react';
import { ChartData } from '../types';

interface DashboardPieChartProps {
  items: Spacecraft[] | undefined;
}

export const DashboardPieChart = ({
  items,
}: DashboardPieChartProps): React.ReactElement => {
  const [data, setData] = useState<ChartData[]>();
  useEffect(() => {
    if (items) {
      const newData: ChartData[] = [];
      const set = new Set<string>();
      items.forEach((item: Spacecraft) => {
        set.add(item.affiliation);
      });

      set.forEach((name: string) => {
        const total = items.filter(
          (item: Spacecraft) => item.affiliation === name,
        ).length;
        newData.push({ x: name.replace('Affiliation ', ''), y: total });
      });
      setData(newData);
    }
  }, [items]);

  const pyscript = `
    import json

    import js
    import pandas as pd
    import plotly
    import plotly.express as px

    ## Get the data
    from pyodide.http import open_url

    url = "https://raw.githubusercontent.com/alanjones2/uk-historical-weather/main/data/Heathrow.csv"
    url_content = open_url(url)

    df = pd.read_csv(url_content)
    df = df[df["Year"] == 2020]


    def plot(chart):
      fig = px.pie(df, values="Month", width=400, height=300, hole=.5)
      graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
      js.Plotly.newPlot("chart1", js.JSON.parse(graphJSON))


    plot("Tmax")
  `;

  return data ? (
    <div
      style={{
        height: '300px',
        width: '400px',
      }}
    >
      <div id="chart1"></div>
      <script type="py" dangerouslySetInnerHTML={{ __html: pyscript }}></script>
    </div>
  ) : (
    <></>
  );
};
