import { Spacecraft } from '@src/types/spacecraft';
import { getPyScriptUrl } from '@src/utils/helpers';
import React, { useEffect, useState } from 'react';
import { ChartData } from '../types';

interface DashboardBarChartProps {
  items: Spacecraft[] | undefined;
}

export const DashboardBarChart = ({
  items,
}: DashboardBarChartProps): React.ReactElement => {
  const [data, setData] = useState<ChartData[]>();
  useEffect(() => {
    if (items) {
      const newData: ChartData[] = [];
      const set = new Set<string>();
      items.forEach((item: Spacecraft) => {
        set.add(item.appearances.toString());
      });

      set.forEach((name: string) => {
        const total = items.filter(
          (item: Spacecraft) => item.appearances.toString() === name,
        ).length;
        newData.push({ x: name, y: total });
      });
      setData(newData);
    }
  }, [items]);

  return data ? (
    <div
      style={{
        height: '300px',
        width: '400px',
      }}
    >
      <div id="dashboard-complex-plot"></div>
      <script
        type="py"
        src={getPyScriptUrl('dashboard-complex-plot.py')}
      ></script>
    </div>
  ) : (
    <></>
  );
};
